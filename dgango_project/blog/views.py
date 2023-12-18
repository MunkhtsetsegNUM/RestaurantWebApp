from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Review
from django.contrib import messages

posts = [
    {
        'user' : 'Munkhtsetseg',
        'review': 'its very delicios',
        'rate': 5,
        'date' : 'December 8, 2023'
    },
    {
        'user' : 'Khula',
        'review': 'Nice',
        'rate': 5,
        'date' : 'December 7, 2023'
    },
    {
        'user' : 'Namuun',
        'review': 'hi',
        'rate': 5,
        'date' : 'December 3, 2023'
    },
    {
        'user' : 'Saruul',
        'review': 'hello',
        'rate': 5,
        'date' : 'December 4, 2023'
    },
]
def all_user(request):
    return HttpResponse('Returning all user')

def home(request):
    context = {
        'posts': Review.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def favorite(request):
    return render(request, 'blog/favorite.html')

def editpass(request):
    return render(request,'blog/editPass.html')

def editprofile(request):
    return render(request,'blog/editProfile.html')


def place(request):
    return render(request,'blog/place.html')

# Create your views here.
