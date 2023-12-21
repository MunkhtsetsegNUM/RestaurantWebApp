from django.urls import path
from . import views
from .views import place_page

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('favorite/', views.favorite_page, name='fav'),
    path('place/<int:pk>', place_page, name='place'),
    path('users/', views.all_user, name='user'),
]