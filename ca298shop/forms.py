from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.db import transaction
from .models import *

class ItemForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'quantity', 'type', 'size', 'colour']
