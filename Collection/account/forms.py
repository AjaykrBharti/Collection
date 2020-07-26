from .models import accounts
from django.forms import ModelForm
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = accounts
        fields = '__all__'

