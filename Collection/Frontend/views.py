from django.shortcuts import render

def index(request):
    context = {}
    return render(request,'Frontend/lessonbase.html',context)
# Create your views here.
