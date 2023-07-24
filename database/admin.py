from django.contrib import admin
from .models import Student_Details,Emp_Details
# Register your models here.
@admin.register(Student_Details)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','std','roll']
    
@admin.register(Emp_Details)
class EmpAdmin(admin.ModelAdmin):
    list_display=['id','name','ocp','org','post']
    