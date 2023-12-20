from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Places, Menu, Review, Users
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

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
        'posts': Places.objects.all()
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


def place(request, pk):
    place = Places.objects.get(id=pk)
    menus = place.menus.all() 
    user = request.session['id']
    user_detail = Users.objects.get(id=user)
    if request.method == "POST":
        star_rating = request.POST.get('rate')
        item_review = request.POST.get('comment')
        item_reviews = Review(author = user_detail, place = place, rate = star_rating, comment = item_review)
        item_review.save()
    context = {
        'place': place,
        'menus': menus,
        'form': form,
    }
    return render(request, 'blog/place.html', context)
