from django.db import models

# Create your models here.

class ChoiceModel(models.Model):
    choice = models.CharField(max_length=15, null=False,default='Default Choice')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice

class ItemModel(models.Model):
    Item = models.CharField(max_length=100,null=False,default='Default Item')
    created_date = models.DateTimeField(auto_now_add=True)
    choices = models.ForeignKey(ChoiceModel,on_delete=models.CASCADE, null=True,default=True)

    def __str__(self):
        return self.Item



