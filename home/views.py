from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    return render(request,'home/home.html')

def menu(request):
    return render(request,'home/menu.html')

def cart(request):
    return render(request,'home/cart.html')

def about(request):
    return render(request,'home/about.html')

def loginAuth(request):
    return render(request,'home/about.html')

def logoutAuth(request):
    logout(request)
    messages.success(request,"Successfully logged out!")
    return redirect('home')

def signupAuth(request):
    return render(request,'home/about.html')