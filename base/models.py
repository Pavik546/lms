from django.db import models
from accounts.models import Student
from course.models import Program



class Payment(models.Model):
    student=models.IntegerField()
    course=models.IntegerField()
    paid=models.BooleanField(default=False)

   