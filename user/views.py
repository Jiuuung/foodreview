from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from user.forms import Customloginform, CreateUser

# Create your views here.


class CustomLogin(LoginView):
    redirect_authenticated_user = True
    authentication_form = Customloginform