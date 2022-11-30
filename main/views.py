import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Restaurant, Review, Menu
from django.utils import timezone
from main.form import RestaurantForm, ReviewForm

# Create your views here.
def list(request):
    restaurant_list= Restaurant.objects.order_by('name')
    context= {'restaurant_list':restaurant_list}
    return render(request, 'main/restaurant_list.html', context)

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk = restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'main/restaurant_detail.html', context)

def add_res(request):
    if request.method=='POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False) #모델에 다른 항목이 추가될 수 있기 때문에 우선은 이렇게 분리해둠.
            restaurant.save()
            menulist= request.POST.getlist('menu[]')
            pricelist = request.POST.getlist('price[]')
            for menu,price in zip(menulist,pricelist):
                menuinstance = Menu(restaurant=restaurant, food=menu, price=price)
                menuinstance.save()

            return redirect('main:list')
    else:
        form = RestaurantForm
    context={'form':form}
    return render(request, 'main/restaurant_add.html', context)

@login_required(login_url='user:login')
def edit_res(request, restaurant_id):
    if request.user.is_superuser:
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        if request.method=="POST":
            form=RestaurantForm(request.POST, instance=restaurant)
            if form.is_valid():
                form.save()
                return redirect('main:detail', restaurant_id)
        else:
            form = RestaurantForm(instance=restaurant)
        context={'form':form}
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
    if request.method=="POST":
        form =ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant=restaurant
            review.reviewer=request.user
            review.create_date=timezone.now()
            review.save()
            return redirect('main:detail', restaurant_id)
    else:
        form =ReviewForm()
    context = {'form':form}
    return render(request, 'main/review_add.html',context)