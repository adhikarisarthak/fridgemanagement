from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django import forms
from .forms import ItemForm, FridgeForm
from .models import Item


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


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'fridge_app/home.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        user = self.request.user
        user_fridges = Fridge.objects.filter(user=user)
        queryset = Item.objects.filter(fridge__in=user_fridges)

        # Get the search query from the request GET parameters
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class FridgeDetailView(LoginRequiredMixin, DetailView):
    model = Fridge


class FridgeCreateView(LoginRequiredMixin, CreateView):
    model = Fridge
    fields = ['name', 'location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        # Redirect to a specific URL after successful form submission
        return redirect('fridge-home')


class FridgeUpdateView(LoginRequiredMixin, UpdateView):
    model = Fridge
    fields = ['name', 'location']
    # form_class = ItemForm
    template_name = 'fridge_app/fridge_update.html'
    success_url = '/fridge/'  # URL to redirect after successful update


class FridgeDeleteView(LoginRequiredMixin, DeleteView):
    model = Fridge
    success_url = '/fridge/'  # URL to redirect after successful update
    template_name = 'fridge_app/fridge_update.html'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']
    success_url = '/items/'  # URL to redirect after successful create

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fridge_list'] = Fridge.objects.all()
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    # fields = ['name', 'category', 'qty', 'fridge', 'expiry_date']
    form_class = ItemForm
    template_name = 'fridge_app/item_update.html'
    success_url = '/items/'  # URL to redirect after successful update

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'  # URL to redirect after successful update
    template_name = 'fridge_app/item_update.html'


def item_delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('items-home')  # Redirect to the list view of items after deletion

    return render(request, 'fridge_app/home.html')


def item_update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST['name']
        qty = request.POST['qty']
        category = request.POST['category']
        fridge = request.POST['fridge']
        # fridge = Fridge.objects.filter(pk=int(request.POST['fridge']))
        expiry_date = request.POST['expiry_date']

        # Update the item object
        item.name = name
        item.qty = qty
        item.category = category

        item.fridge = fridge
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

    def get_queryset(self):
        user = self.request.user
        queryset = Fridge.objects.filter(user=user)
        return queryset


def sort_category(request):
    user = request.user
    item_list = Item.objects.filter(fridge__user=user).order_by('category')
    context = {
        'item_list': item_list,
        'fridge_list': Fridge.objects.filter(user=user),
        'title': 'Category',
    }
    return render(request, 'fridge_app/sortCategory.html', context)


def expired(request):
    user = request.user
    context = {
        'item_list': Item.objects.filter(fridge__user=user, expiry_date__lt=datetime.now()),
        'fridge_list': Fridge.objects.filter(user=user),
        'title': 'Expired',
    }
    return render(request, 'fridge_app/expired.html', context)


def shopping(request):
    user = request.user
    context = {
        'item_list': Item.objects.filter(fridge__user=user, expiry_date__lt=datetime.now()),
        'fridge_list': Fridge.objects.filter(user=user),
        'title': 'Expired',
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
