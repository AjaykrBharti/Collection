from django.shortcuts import render
from .models import UploadImage
from .forms import  UploadForm

def index(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'imageupload/upload.html',context)

# Create your views here.
