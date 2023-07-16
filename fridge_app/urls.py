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

)
from . import views

urlpatterns = [
    # path('', views.home, name='fridge-home'),
    path('items/', ItemListView.as_view(), name='items-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item_create'),
    path('fridge/', FridgeListView.as_view(), name='fridge-home'),
    path('fridge/<int:pk>/', FridgeDetailView.as_view(), name='fridge-detail'),
    path('fridge/new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('about/', views.about, name='fridge-about'),
    path('item/expired', views.expired, name='fridge-expired'),
    path('shopping', views.shopping, name='fridge-shopping'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    # path('item/<int:pk>/update/', views.item_update_view, name='item_update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
