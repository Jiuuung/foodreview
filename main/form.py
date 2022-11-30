from django import forms
from main.models import Restaurant, Review, Menu

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'introduce','opentime','closetime']

        labels ={
            'name':'식당 이름',
            'introduce': '소개',
            'opentime':'시작시간',
            'closetime':'종료시간',
        }
