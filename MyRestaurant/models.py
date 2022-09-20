from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.

#Model for Menu
class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images",default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_json = models.JSONField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    
    