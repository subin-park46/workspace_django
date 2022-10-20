from django.shortcuts import render
from .models import MyBoard

def index(request):
    return render(request, "index.html", {"list": MyBoard.objects.all().order_by('-id')}) # id 기준으로 정렬, -는 DESC
