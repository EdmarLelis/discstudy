from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')
