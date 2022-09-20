from django.contrib import admin
from .models import Food,Order

# Register your models here.
admin.site.register((Food))

@admin.register(Order)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user')

