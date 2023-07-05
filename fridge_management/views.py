from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import redirect
from datetime import date
from fridge_management.models import Item, Fridge, ItemFridge

# Get the item objects from the database or create new ones if needed
item_apple = Item(name='apple', category='fruit')
item_banana = Item(name='banana', category='fruit')
item_egg = Item(name='egg', category='dairy')

# Get the fridge objects from the database or create new ones if needed
fridge1 = Fridge(name='Dining Room Fridge', location='Dining Room')
fridge2 = Fridge(name='Garage Fridge', location='Garage')
fridge3 = Fridge(name='Garage Deep Freezer', location='Garage')

# Create ItemFridge entries to associate items with fridges
fridge1_content = ItemFridge(item=item_apple, fridge=fridge1, quantity=5, expiration_date=date(2023, 12, 31))
fridge2_content = ItemFridge(item=item_banana, fridge=fridge2, quantity=3, expiration_date=date(2023, 12, 15))
fridge3_content = ItemFridge(item=item_egg, fridge=fridge3, quantity=10, expiration_date=date(2023, 12, 10))

members = [
    {
        'name': 'Kyaw Min Thu',
        'id': 'gb6499'
    },
    {
        'name': 'Nayan Pai',
        'id': 'bp3398'
    },
    {
        'name': 'Sarthak Adhikari',
        'id': 'bv9292'
    },
    {
        'name': 'Triet Nguyen',
        'id': 're2653'
    },
    {
        'name': 'Yichao Hao',
        'id': 'ur5215'
    }
]

# Create your views here.


def home(request):
    context = {
        'fridge1_content': fridge1_content
    }
    return render(request, 'fridge_management/fm-main.html', context)


def about(request):
    context = {
        'members': members
    }
    return render(request, 'fridge_management/about.html', context)


def wiki(request):
    return redirect('https://github.com/adhikarisarthak/fridgemanagement/wiki')
