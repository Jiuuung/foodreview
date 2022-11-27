from django.shortcuts import render, get_object_or_404, redirect
from main.models import Restaurant, Review
from main.form import RestaurantForm

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
            return redirect('main:list')
    else:
        form = RestaurantForm
    context={'form':form}
    return render(request, 'main/restaurant_add.html', context)
