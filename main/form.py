from django import forms
from main.models import Restaurant, Review

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'introduce']

        labels ={
            'name':'식당 이름',
            'introduce': '소개',
        }