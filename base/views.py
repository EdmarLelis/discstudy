from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def home(request):
    return render(request, 'home.html')


def rooms(request):
    return render(request, 'rooms.html')
