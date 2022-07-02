from statistics import mode
from django.db import models

# Create your models here.
class stu_model(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_marks = models.CharField(max_length=20)