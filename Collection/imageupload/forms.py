from django.forms import  ModelForm
from django import  forms

from .models import UploadImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'



