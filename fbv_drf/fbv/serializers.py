from rest_framework import serializers
from database.models import Student_Details

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student_Details
        fields='__all__'