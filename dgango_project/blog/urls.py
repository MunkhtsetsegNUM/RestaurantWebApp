from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hi'),
    path('about/', views.about, name='about'),
    path('editpass/', views.editpass, name='editpass'),
    path('favorite/', views.favorite, name='fav'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('login/', views.login, name='login'),
    path('place/', views.place, name='place'),
    path('signup/', views.signup, name='signup'),
    path('users/', views.all_user, name='user'),
]