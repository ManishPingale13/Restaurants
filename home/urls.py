from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('cart',views.cart,name="cart"),
    path('menu',views.menu,name="menu"),
    path('orders',views.orders,name="orders"),
    path('about',views.about,name="about"),
    path('login',views.loginAuth,name="login"),
    path('logout',views.logoutAuth,name="logout"),
    path('signup',views.signupAuth,name="signup"),
]
