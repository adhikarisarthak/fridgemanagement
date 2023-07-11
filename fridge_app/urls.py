from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    FridgeListView,
    FridgeDetailView,
    FridgeCreateView,
)
from . import views

urlpatterns = [
    # path('', views.home, name='fridge-home'),
    path('', ItemListView.as_view(), name='fridge-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item_create'),
    path('fridge/', FridgeListView.as_view(), name='fridge-home'),
    path('fridge/<int:pk>/', FridgeDetailView.as_view(), name='fridge-detail'),
    path('fridge/new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('about/', views.about, name='fridge-about'),
    path('item/expired', views.expired, name='fridge-expired'),
    path('shopping', views.shopping, name='fridge-shopping'),
    path('item/update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),

]
