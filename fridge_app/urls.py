from django.urls import path
from .views import ItemListView
from . import views


urlpatterns = [
    path('', ItemListView.as_view(), name='fridge-home'),
    # path('', views.home, name='fridge-home'),#
    path('about/', views.about, name='fridge-about'),
]
