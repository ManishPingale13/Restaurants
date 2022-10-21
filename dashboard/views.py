import json

import boto3
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.models import Food, Order

# Create your views here.


def deleteFood(request):
    id = request.GET.get('id', '')
    if id.strip():
        food = Food.objects.get(id=id)
        food.delete()
        messages.success(request, "Successfully deleted")
        return HttpResponse(json.dumps({
            "status": "success",
        }))
    return redirect('foods')


def customers(request):
    return render(request, 'dashboard/customers.html')


def upload(image):
    session = boto3.Session(
        aws_access_key_id='AKIAS6ENUTQNOTQ45WWF',
        aws_secret_access_key='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',
    )
    s3 = session.resource('s3')
    s3.Bucket('mydjango-static-bucket').put_object(Key='static/images/%s' %
                                                   image.name, Body=image)


def foods(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        foodId = request.POST.get('FoodId')
        image = request.FILES.get("image", '')
        
        #If item exists then updates, else creates new item
        try:
            food = Food.objects.get(id=foodId)
            # Updating the existing food item
            if food:
                food.name, food.price = name, price
                if image:
                    food.image = image
                    upload(image)
                food.save()
                messages.success(request, "Item has been updated!")

        # Creating new food item
        except Food.DoesNotExist:
            newFood = Food(name=name, price=price, image=image)
            upload(image)
            newFood.save()
            messages.success(request, "New item successfully added!")

        return redirect('foods')
    menu = Food.objects.all()
    return render(request, 'dashboard/foods.html', {"foods": menu})


def updateStatus(request):
    id = request.POST.get('identifier')
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
            if pending == 'true':
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
