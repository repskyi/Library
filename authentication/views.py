from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import BaseBackend

from .forms import *
from .models import CustomUser


# Create your views here.
def loginPage(request):
    user = request.user    
    if user.is_authenticated:
        return redirect('home')
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if form.is_valid():
            if user:
                login(request, user)
                messages.success(request, "You successful Logged In")
                return redirect('home')
            else: 
                 messages.error(request, "Invilid Email or Password")
        else:
            messages.error(request, "Enter a valid email address.")

    return render(request, 'authentication/login.html', {'title': 'Login','form':form})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registration(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        password = request.POST.get('password1') 
        email = request.POST.get('email') 
        
        if form.is_valid():
            CustomUser.create(email, password, first_name, last_name, middle_name)
            messages.success(request, f'You have been successfully registered {email} {password} {first_name} {last_name} {middle_name}')
            return redirect('login')
        else:
            messages.error(request, form.errors)
        
    context = {'title': 'Registration', 'form': form}
    return render(request, 'authentication/registration.html', context)