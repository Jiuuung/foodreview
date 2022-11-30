from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.list , name = 'list'),
    path('<int:restaurant_id>/', views.detail , name ='detail'),
    path('addres/', views.add_res, name='restaurant_add'),
    path('editres/<int:restaurant_id>/', views.edit_res, name ='restaurant_edit'),
    path('deleteres/<int:restaurant_id>/', views.delete_res, name ='restaurant_delete'),
    path('recommendres/',views.restaurantrecommend, name='restaurant_recommend'),
    path('addrev/<int:restaurant_id>/', views.add_rev, name ='review_add'),
]