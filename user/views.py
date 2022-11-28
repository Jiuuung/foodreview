import json
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import Customloginform, CreateUser

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('user:logout')
    if request.method=="POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user= authenticate(username=username, password=password)
            login(request, user)
            return redirect('user:signup_done')
    else:
        form=CreateUser()
    context={'form':form}
    return render(request,'user/signup.html',context)

def signupdone(request):
    return render(request, 'user/signup_done.html')

def checknicknamemultiple(request):
    if get_user_model().objects.filter(nickname=request.POST.get('nickname',None)).exists() or request.POST.get('nickname',None)=='':
        message="사용불가능한 닉네임입니다."
        context={'message':message, 'value':False}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
        message = "사용가능한 닉네임입니다."
        context ={'message':message,'value':True}
        return HttpResponse(json.dumps(context), content_type="application/json")

class CustomLogin(LoginView):
    redirect_authenticated_user = True
    authentication_form = Customloginform

def mypage(request, user_id):
    user=get_object_or_404(get_user_model(), pk=user_id)
    context={'user':user}
    return render(request, 'user/mypage.html',context)