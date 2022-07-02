from rest_framework import serializers
from fvb_app.models import studentTable
class serial(serializers.ModelSerializer):
    class Meta:
        model = studentTable
        fields = ['stu_id','stu_name','stu_marks']