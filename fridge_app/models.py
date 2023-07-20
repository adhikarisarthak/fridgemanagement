from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime


class Fridge(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_user_fridges(user):
        return Item.objects.filter(user=user)


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    qty = models.IntegerField()
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)
    expiry_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

    def is_expired(self):
        return self.expiry_date < datetime.now().date()

    def fridge_name(self):
        return self.fridge.name

    def __str__(self):
        return self.name

    """


    @staticmethod
    def remove_expired_items():
        Item.objects.filter(expiry_date__lt=models.DateTimeField(default=timezone.now())).delete()

    @staticmethod
    def search_items(query):
        return Item.objects.filter(name__icontains=query)

    @staticmethod
    def generate_shopping_list():
        items = Item.objects.filter(expiry_date__gte=models.DateTimeField(default=timezone.now))
        shopping_list = []
        for item in items:
            if item.qty > 0:
                shopping_list.append(item.name)
                item.qty -= 1
                item.save()
        return shopping_list
        
        """
