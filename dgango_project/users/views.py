from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request,'users/register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        pass1 = request.POST.get['password']
        
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            redirect('blog/editprofile')
        else:
            messages.error(request, "Bad")
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')
