from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='fridge-home'),
    path('about/', views.about, name='fridge-about'),
]
