from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    FridgeListView,
    FridgeDetailView,
    FridgeCreateView,
    FridgeUpdateView,
    FridgeDeleteView,

)
from . import views

urlpatterns = [
    # path('', views.home, name='fridge-home'),
    path('items/', ItemListView.as_view(), name='items-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item_create'),
    path('fridge/', FridgeListView.as_view(), name='fridge-home'),
    path('fridge/<int:pk>/', FridgeDetailView.as_view(), name='fridge_detail'),
    path('fridge/<int:pk>/update', FridgeUpdateView.as_view(), name='fridge_update'),
    path('fridge/new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('fridge/<int:pk>/delete/', FridgeDeleteView.as_view(), name='fridge_delete'),
    path('about/', views.about, name='fridge-about'),
    path('item/expired', views.expired, name='item-expired'),
    path('item/sort/', views.sort_category, name='item-sorted'),
    path('shopping', views.shopping, name='fridge-shopping'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    # path('item/<int:pk>/update/', views.item_update_view, name='item_update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    # path('item/<int:pk>/delete/', views.item_delete_view, name='item_delete'),

]
