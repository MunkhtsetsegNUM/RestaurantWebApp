from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('editpass/', views.editpass, name='editpass'),
    path('favorite/', views.favorite, name='fav'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('place/', views.place, name='place'),
    path('users/', views.all_user, name='user'),
]