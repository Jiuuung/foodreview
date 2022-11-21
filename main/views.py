from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("카이스트 주변 음식 리뷰 서비스 입니디.")