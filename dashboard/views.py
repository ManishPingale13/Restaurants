from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def customers(request):
    return render(request,'dashboard/customers.html')

def foods(request):
    return render(request,'dashboard/foods.html')

@login_required
def dashboard(request):
    if request.user.is_superuser:
        print("In Dashboard")
        return render(request,"dashboard/orders.html")
    else:
        return render(request,"403.html")
