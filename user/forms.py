from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class CreateUser(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=["username", "password1", "password2", "nickname",]
        labels={
            'username':'아이디',
            'nickname':'닉네임',
        }

class Customloginform(AuthenticationForm):
    username = UsernameField(
        label='아이디',
    )