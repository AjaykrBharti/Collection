from django.contrib import admin
from .models import QuestionModel,QuizModel
# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(QuizModel)