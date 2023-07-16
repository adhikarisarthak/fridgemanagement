from django import forms
from .views import Item


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
