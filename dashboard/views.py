from django.shortcuts import render

# Create your views here.

def dashboard(request):
    print("In Dashboard")
    return render(request,"dashboard/dashboard.html")
