from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Places, Menu, Review, Users
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
import logging

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

def home_page(request):
    star_range = range(1, 6)
    context = {
        'posts': Places.objects.all(),
        'star_range': star_range
    }
    return render(request, 'blog/home.html', context)

def about(request):
    try:
        # Some process
        logging.info('Successfully completed the process.')
    except Exception as e:
        # Handle exceptions
        logging.error(f'An error occurred: {str(e)}')
    return render(request, 'blog/about.html')

def favorite_page(request):
    return render(request, 'blog/favorite.html')

def editprofile_page(request):
    return render(request,'blog/editProfile.html')

def place_page(request, pk):
    place = Places.objects.get(id=pk)
    menus = place.menus.all() 
    user = request.user
    star_range = range(1, 6)
    if request.method == "POST":
        star_rating = request.POST.get('rate')
        item_review = request.POST.get('comment')
        item_reviews = Review(author = user, place = place, rate = star_rating, comment = item_review)
        item_reviews.save()
        
    reviews = Review.objects.filter(place=place)
        
    context = {
        'place': place,
        'menus': menus,
        'reviews': reviews,
        'star_range': star_range
    }
    return render(request, 'blog/place.html', context)
