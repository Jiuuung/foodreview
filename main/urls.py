from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.list , name = 'list'),
    path('<int:restaurant_id>/', views.detail , name ='detail'),
    path('addres/', views.add_res, name='restaurant_add'),
]