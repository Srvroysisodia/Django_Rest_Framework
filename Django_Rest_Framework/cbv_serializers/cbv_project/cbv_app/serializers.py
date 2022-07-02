from cbv_app.models import stu_model
from rest_framework import serializers

class serial(serializers.ModelSerializer):
    class Meta:
        model = stu_model
        fields = '__all__'