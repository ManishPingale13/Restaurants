import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Order, Food
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'home/home.html')


@login_required
def orders(request):
    if request.method == "POST":
        foodJson = request.POST.get('foodJson')
        user = request.user
        order = Order(user=user, food_json=foodJson)
        order.save()
        messages.success(request, "Order has been placed!")

    order = Order.objects.all()
    orders=[]
    for i in order:        
        orders.append({
            'id':i.id,
            'foods':json.loads(i.food_json),
        })        
    
    return render(request, 'home/orders.html',{'orders':orders})


def menu(request):
    food = Food.objects.all()
    return render(request, 'home/menu.html', {'foods': food})


def cart(request):
    return render(request, 'home/cart.html')


def about(request):
    return render(request, 'home/about.html')


def loginAuth(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpass']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect("home")
    else:
        return render(request, 'home/login.html')


@login_required
def logoutAuth(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('home')


def signupAuth(request):
    # Get the post parameters
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']

        # check for errorneous input
        if len(username) > 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')

        # Create the user
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, "Your account has been successfully created!")
        return redirect('home')

    else:
        return render(request, 'home/signup.html')
