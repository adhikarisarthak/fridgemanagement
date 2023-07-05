from django.urls import path
from . import views

# URL Patterns


# Item Patterns
urlpatterns = [
    path('', views.home, name = 'fm-home'),
    path('about/', views.about, name = 'fm-about'),
    path('wiki/', views.wiki, name = 'fm-wiki')
    #path('/items', ),
    #path('api', include("fridge_management.urls"))
]
# Fridge Patterns

# Item Fridge Patterns

