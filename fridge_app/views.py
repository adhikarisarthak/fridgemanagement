from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'fridge_app/home.html'
    context_object_name = 'item_list'


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class FridgeDetailView(LoginRequiredMixin, DetailView):
    model = Fridge


class FridgeCreateView(LoginRequiredMixin, CreateView):
    model = Fridge
    fields = ['name', 'location']


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fridge_list'] = Fridge.objects.all()
        return context


class ItemForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']
    # form_class = ItemForm
    template_name = 'fridge_app/item_update.html'
    success_url = '/items/'  # URL to redirect after successful update


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'  # URL to redirect after successful update
    template_name = 'fridge_app/item_update.html'


def item_update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST['name']
        qty = request.POST['qty']
        category = request.POST['category']
        fridge = request.POST['fridge']
        expiry_date = request.POST['expiry_date']

        # Update the item object
        item.name = name
        item.qty = qty
        item.category = category
        # item.fridge = fridge.pk
        item.expiry_date = expiry_date
        item.save()

        # Redirect to the item detail view or any other desired page
        return redirect('items-home')

    context = {'item': item}
    return render(request, 'fridge_app/item_update.html', context)


class FridgeListView(LoginRequiredMixin, ListView):
    model = Fridge
    template_name = 'fridge_app/fridges.html'
    context_object_name = 'fridge_list'


class FridgeDetailView(LoginRequiredMixin, DetailView):
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
