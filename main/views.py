import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Restaurant, Review, Menu
from django.utils import timezone
from main.form import RestaurantForm, ReviewForm
from django.contrib.auth import get_user_model

# Create your views here.
def list(request):
    restaurant_list= Restaurant.objects.order_by('name')
    context= {'restaurant_list':restaurant_list}
    return render(request, 'main/restaurant_list.html', context)

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk = restaurant_id)
    score=float(restaurant.score)
    count = float(restaurant.review_set.count())
    if count!=0:
        total_score= round(score/count,1)
    else:
        total_score=0
    context = {'restaurant': restaurant, 'reviewlist':restaurant.review_set.all(), 'total_score':total_score}
    return render(request, 'main/restaurant_detail.html', context)

def add_res(request):
    if request.method=='POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            menulist = request.POST.getlist('menu[]')
            pricelist = request.POST.getlist('price[]')
            if not len(set(menulist))==len(menulist):
                form.errors['__all__'] = form.error_class(["메뉴이름은 중복될 수 없습니다."])
                context = {'form': form}
                return render(request, 'main/restaurant_add.html', context)
            restaurant = form.save(commit=False) #모델에 다른 항목이 추가될 수 있기 때문에 우선은 이렇게 분리해둠.
            restaurant.save()
            for menu,price in zip(menulist,pricelist):
                menuinstance = Menu(restaurant=restaurant, food=menu, price=price)
                menuinstance.save()
            return redirect('main:list')
    else:
        form = RestaurantForm()

    context={'form':form}
    return render(request, 'main/restaurant_add.html', context)

@login_required(login_url='user:login')
def edit_res(request, restaurant_id):
    if request.user.is_superuser:
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        if request.method=="POST":
            form=RestaurantForm(request.POST, instance=restaurant)
            if form.is_valid():
                foodlist = restaurant.menu_set.all()
                menulist = request.POST.getlist('menu[]')
                pricelist = request.POST.getlist('price[]')
                for menu in foodlist:
                    menu.delete()
                editres=form.save()
                for menu, price in zip(menulist, pricelist):
                    menuinstance = Menu(restaurant=editres, food=menu, price=price)
                    menuinstance.save()
                return redirect('main:detail', restaurant_id)
        else:
            form = RestaurantForm(instance=restaurant)
        context={'form':form, 'menulist':restaurant.menu_set.all(), }
        return render(request, 'main/restaurant_add.html',context)
    else:
        return HttpResponseNotAllowed('Only Superuser is possible')
@login_required(login_url='user:login')
def delete_res(request, restaurant_id):
    if request.user.is_superuser:
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        restaurant.delete()
        return redirect('main:list')
    else:
        return HttpResponseNotAllowed('Only Superuser is possible')

@login_required(login_url='user:login')
def restaurantrecommend(request):
    restaurant=get_object_or_404(Restaurant, pk=request.POST.get('restaurant_id',None))
    if restaurant.recommend.filter(id=request.user.id).exists():
        restaurant.recommend.remove(request.user)
        message="추천을 취소합니다."
    else:
        restaurant.recommend.add(request.user)
        message="추천합니다."
    context={'recommend_count':restaurant.recommend.count(), 'message':message}
    return HttpResponse(json.dumps(context),content_type='application/json')


@login_required(login_url='user:login')
def add_rev(request, restaurant_id):
    restaurant=get_object_or_404(Restaurant, pk=restaurant_id)
    menulist=restaurant.menu_set.all()
    if request.method=="POST":
        form =ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            menu=request.POST.get('menu')
            review.menu=get_object_or_404(Menu, pk=menu)
            review.star=float(request.POST.get('star'))
            review.restaurant=restaurant
            review.reviewer=request.user
            user =get_object_or_404(get_user_model(), pk=request.user.id)
            user.reviewcount=int(request.user.reviewcount + 1)
            user.save()
            review.create_date=timezone.now()
            review.save()
            restaurant.score +=float(request.POST.get('star'))
            restaurant.save()
            return redirect('main:detail', restaurant_id)
    else:
        form =ReviewForm()
    context = {'form':form, 'menulist':menulist,}
    return render(request, 'main/review_add.html',context)

@login_required(login_url='user:login')
def edit_rev(request, review_id):
    review=get_object_or_404(Review, pk=review_id)
    restaurant= get_object_or_404(Restaurant, pk=review.restaurant.id)
    menulist = restaurant.menu_set.all()
    if request.user == review.reviewer:
        if request.method=="POST":
            star=review.star
            form =ReviewForm(request.POST, instance=review)
            if form.is_valid():
                restaurant = review.restaurant
                editreview = form.save(commit=False)
                editreview.create_date=timezone.now()
                menu = request.POST.get('menu')
                editreview.menu = get_object_or_404(Menu, pk=menu)
                editreview.star = float(request.POST.get('star'))
                editreview.save()
                restaurant.score -= float(star)
                restaurant.score +=float(request.POST.get('star'))
                restaurant.save()
                return redirect('main:detail', restaurant.id)
        else:
            form =ReviewForm(instance=review)
        context = {'form':form,'review':review, 'star':review.star, 'menulist':menulist,}
        return render(request, 'main/review_add.html',context)
    else:
        return HttpResponseNotAllowed('Only Superuser is possible')


@login_required(login_url='user:login')
def delete_rev(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user==review.reviewer:
        user = get_object_or_404(get_user_model(), pk=request.user.id)
        user.reviewcount = int(request.user.reviewcount - 1)
        user.save()
        restaurant_id=review.restaurant.id
        restaurant =get_object_or_404(Restaurant, pk=restaurant_id)
        restaurant.score-=int(review.star)
        restaurant.save()
        review.delete()
        return redirect('main:detail', restaurant_id)
    else:
        return HttpResponseNotAllowed('Only Superuser is possible')