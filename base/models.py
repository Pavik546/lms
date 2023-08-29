from django.db import models
from accounts.models import Student
from course.models import Program



class Payment(models.Model):
    student=models.IntegerField()
    course=models.IntegerField()
    paid=models.BooleanField(default=False)

class Ymd(models.Model):
    student = models.CharField(max_length=100)
    courset = models.CharField(max_length=100)
    coursep = models.CharField(max_length=100)
    quizc = models.CharField(max_length=100)
    quizt = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)  # Add this line
    maxscore = models.IntegerField(default=0)

   