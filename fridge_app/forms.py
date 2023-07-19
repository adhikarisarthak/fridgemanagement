from django import forms
from .views import Item, Fridge


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class FridgeForm(forms.ModelForm):
    class Meta:
        model = Fridge
        fields = '__all__'
