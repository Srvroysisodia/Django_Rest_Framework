from django.db import models

# Create your models here.
class Student_Details(models.Model):
    name=models.CharField(max_length=250)
    std = models.IntegerField()
    roll=models.IntegerField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Emp_Details(models.Model):
    name=models.CharField(max_length=250)
    ocp = models.IntegerField()
    post=models.CharField(max_length=250)
    org = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    
    