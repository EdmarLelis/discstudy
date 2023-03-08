from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':1, 'name':'Web Develop'},
    {'id':1, 'name':'Learn C#'},
]




def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
