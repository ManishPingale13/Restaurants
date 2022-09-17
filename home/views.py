from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home/home.html')

def menu(request):
    return render(request,'home/menu.html')

def cart(request):
    return render(request,'home/cart.html')

def about(request):
    return render(request,'home/about.html')