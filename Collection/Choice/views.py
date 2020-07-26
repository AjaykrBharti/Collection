from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ChoiceModel,ItemModel
from .forms import ChoiceForm,ItemForm
# Create your views here.

def index(request):
    choiceform = ChoiceForm()
    if request.method == 'POST':
        choiceform = ChoiceForm(request.POST)
        if choiceform.is_valid():
            choiceform.save()
            return redirect('choice')
    itemform = ItemForm()
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            itemform.save()
            return redirect('choice')
    items = ItemModel.objects.all()
    context = {'choiceform':choiceform,'itemform':itemform, 'items':items}
    return render(request,'Choice/index.html',context)
