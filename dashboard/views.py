import json
from tkinter.messagebox import NO
from turtle import pen

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Order

# Create your views here.

def customers(request):
    return render(request, 'dashboard/customers.html')


def foods(request):
    return render(request, 'dashboard/foods.html')


def updateStatus(request):
    id=request.POST['identifier']
    order = Order.objects.all().filter(id=id)[0]
    order.is_delivered = not order.is_delivered
    order.save() 
    return HttpResponse(json.dumps({'status': 'success'}))


@login_required
def orders(request):
    if request.user.is_superuser:
        if request.method == "POST":
            pending = request.POST.get('pending')
            if pending is None:
                return updateStatus(request)
            orders = []
            if pending=='true':
                orders = Order.objects.all().filter(is_delivered=False).order_by('-id')
            else:
                orders = Order.objects.all().filter(is_delivered=True).order_by('-id')
            fetchedOrders = []
            for order in orders:
                fetchedOrders.append({
                    'id': order.id, 'user': order.user.username,
                    'food_json': order.food_json, 'is_delivered': order.is_delivered
                })
            response = json.dumps({
                'status': 'success',
                'orders': fetchedOrders,
            })
            return HttpResponse(response)
        else:
            orders = Order.objects.all().order_by('-id')
            return render(request, "dashboard/orders.html", {'orders': orders})
    else:
        return render(request, "403.html")
