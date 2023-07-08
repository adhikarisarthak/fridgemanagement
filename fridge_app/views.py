from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Item, Fridge

item_list = [
    {
        "id": 1,
        "name": "Apple",
        "category": "Fruits",
        "qty": 10,
        "fridge_id": 1,
        "expiry_date": "2023-03-09T22:00:00"
    },
    {
        "id": 2,
        "name": "Beef",
        "category": "Meat",
        "qty": 1,
        "fridge_id": 1,
        "expiry_date": "2023-03-10T22:00:00"
    },
    {
        "id": 3,
        "name": "Eggs",
        "category": "Diary",
        "qty": 12,
        "fridge_id": 1,
        "expiry_date": "2023-03-09T22:00:00"
    },
    {
        "id": 4,
        "name": "Milk",
        "category": "Diary",
        "qty": 2,
        "fridge_id": 2,
        "expiry_date": "2023-03-19T22:00:00"
    },
]

members = [
    {
        "name": "Kyaw Min Thu",
        "id": "gb6499",
    },
    {
        "name": "Nayan Pai",
        "id": "bp3398",
    },
    {
        "name": "Sarthak Adhikari",
        "id": "bv9292",
    },
    {
        "name": "Yichao Hao",
        "id": "ur5215",
    }
]


# Create your views here.
def home(request):
    context = {
        'item_list': Item.objects.all(),
        'fridge_list': Fridge.objects.all(),
        'title': 'Home',
    }
    return render(request, 'fridge_app/home.html', context)


class ItemListView(ListView):
    model = Item
    template_name = 'fridge_app/home.html'
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']


class FridgeListView(ListView):
    model = Fridge
    template_name = 'fridge_app/fridges.html'
    context_object_name = 'fridge_list'


class FridgeDetailView(DetailView):
    model = Fridge


class FridgeCreateView(CreateView):
    model = Fridge


def sort_category(request):
    context = {
        'item_list': Item.objects.all(),
        'fridge_list': Fridge.objects.all(),
        'title': 'Category',
    }
    return render(request, 'fridge_app/sortCategory.html', context)


def expired(request):
    context = {
        'item_list': Item.objects.all(),
        'fridge_list': Fridge.objects.all(),
        'title': 'Expired',
    }
    return render(request, 'fridge_app/expired.html', context)


def fridges(request):
    context = {
        'item_list': Item.objects.all(),
        'fridge_list': Fridge.objects.all(),
        'title': 'Fridges',
    }
    return render(request, 'fridge_app/fridges.html', context)


def about(request):
    context = {
        'members': members,
        'title': 'About',
    }
    return render(request, 'fridge_app/about.html', context)
