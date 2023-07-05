from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)


class Fridge(models.Model):

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete= models.CASCADE)


class ItemFridge(models.Model):

    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    fridge = models.ForeignKey(Fridge, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    expiration_date = models.DateField()

