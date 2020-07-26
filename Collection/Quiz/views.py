from django.shortcuts import render
from django.http import HttpResponse
from .models import QuizModel,QuestionModel

# Create your views here.
def index(request):
    # query = QuizModel.objects.all()[0]
    # print(query)
    # questions = query.quizmodel_set.all()
    # context = {'questions':questions}
    # return render(request,'Quiz/index.html',context)
    return HttpResponse("Hello World")