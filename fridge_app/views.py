from django.shortcuts import render
from datetime import datetime
from django import forms

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Item, Fridge

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
"""
def home(request):
    context = {
        'item_list': Item.objects.all(),
        'fridge_list': Fridge.objects.all(),
        'title': 'Home',
    }
    for i in Item.objects.all():
        print(i.expiry_date)
    return render(request, 'fridge_app/home.html', context)
"""


class ItemListView(ListView):
    model = Item
    template_name = 'fridge_app/home.html'
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item


class FridgeDetailView(DetailView):
    model = Fridge


class FridgeCreateView(CreateView):
    model = Fridge
    fields = ['name', 'location']


class ItemCreateView(CreateView):
    model = Item
    # template_name = 'fridge_app/item_form.html'
    fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fridge_list'] = Fridge.objects.all()
        return context


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'fridge_app/item_update.html'
    success_url = '/item/list'  # URL to redirect after successful update


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
        'item_list': Item.objects.filter(expiry_date__lt=datetime.now()),
        'fridge_list': Fridge.objects.all(),
        'title': 'Expired',
    }
    return render(request, 'fridge_app/expired.html', context)


def shopping(request):
    context = {
        'item_list': Item.objects.filter(expiry_date__lt=datetime.now()),
        'fridge_list': Fridge.objects.all(),
        'title': 'Shopping',
    }
    return render(request, 'fridge_app/shopping_list.html', context)


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
