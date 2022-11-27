from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Review

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
    return redirect('main/restaurant_add.html')
