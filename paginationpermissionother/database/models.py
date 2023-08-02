from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=250)
    roll=models.IntegerField()
    std=models.IntegerField()
    
    def __str__(self):
        return self.name