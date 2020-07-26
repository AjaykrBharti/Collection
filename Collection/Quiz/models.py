from django.db import models

# Create your models here.



class QuestionModel(models.Model):
    Question = models.TextField(max_length=400)
    OptionOne = models.CharField(max_length=20)
    OptionTwo = models.CharField(max_length=20)
    OptionThree = models.CharField(max_length=20)
    OptionFour = models.CharField(max_length=20)

    def __str__(self):
        return self.Question

class QuizModel(models.Model):
    QuizName = models.CharField(max_length=20)
    Questions = models.ManyToManyField(QuestionModel)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.QuizName