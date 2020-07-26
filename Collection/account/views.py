from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import accounts

# Create your views here.
def index(request):
    account = accounts.objects.all()
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            form = AccountForm()
    context = {'form':form,'account':account}
    return render(request,'account/index.html',context)

def update(request,pk):
    account = accounts.objects.get(id = pk)
    form = AccountForm(instance=account)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    context = {'form':form}
    return render(request,'account/index.html',context)


def delete(request,pk):
    account = accounts.objects.get(id = pk)
    account.delete()

    return redirect('accounts')