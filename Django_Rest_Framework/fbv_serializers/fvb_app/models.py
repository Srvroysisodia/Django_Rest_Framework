
from django.db import models

# Create your models here.
class studentTable(models.Model):
    stu_id= models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=20)
    stu_marks = models.CharField(max_length=10)