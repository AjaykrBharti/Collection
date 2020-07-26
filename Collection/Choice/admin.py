from django.contrib import admin

# Register your models here.
from .models import ChoiceModel,ItemModel

admin.site.register(ChoiceModel)
admin.site.register(ItemModel)
