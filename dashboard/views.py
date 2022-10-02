import json
from turtle import pendown
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Order
from django.http import HttpResponse


# Create your views here.

def customers(request):
    return render(request, 'dashboard/customers.html')


def foods(request):
    return render(request, 'dashboard/foods.html')


@login_required
def orders(request):
    if request.user.is_superuser:
        if request.method == "POST":
            print(request.POST.get('pending'))
            pending = request.POST.get('pending')
            if pending:
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
