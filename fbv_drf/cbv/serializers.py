from database.models import  Emp_Details
from rest_framework import serializers

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp_Details
        fields='__all__'