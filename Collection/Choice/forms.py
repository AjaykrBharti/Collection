from django import forms
from django.forms import ModelForm
from .models import ItemModel,ChoiceModel

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['Item','choices']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = ChoiceModel
        fields = ['choice']