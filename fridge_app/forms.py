from django import forms
from .models import Item, Fridge


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['fridge'].queryset = Fridge.objects.filter(user=user)


class FridgeForm(forms.ModelForm):
    class Meta:
        model = Fridge
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(FridgeForm, self).__init__(*args, **kwargs)
        self.fields['fridge'].queryset = Fridge.objects.filter(user=user)
