from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

app_name='user'

urlpatterns=[
    path('login/', views.CustomLogin.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup , name='signup'),
]