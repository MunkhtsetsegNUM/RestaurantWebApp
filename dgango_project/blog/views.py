from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from django.http import HttpResponse

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

def login(request):
    return render(request,'blog/login.html')

def place(request):
    return render(request,'blog/place.html')

def signup(request):
    return render(request,'blog/signup.html')

# Create your views here.
