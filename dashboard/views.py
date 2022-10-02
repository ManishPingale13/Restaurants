from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        print("In Dashboard")
        return render(request,"dashboard/dashboard.html")
    else:
        return render(request,"403.html")
