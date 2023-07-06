from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Fridge(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    qty = models.IntegerField()
    fridge_id = models.ForeignKey(Fridge, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()
