from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from database.models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .pagination import CustomLimitOffSetPagination
# Create your views here.
class StudentCreateListApiView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_class=[BasicAuthentication]
    permission_class=[IsAuthenticated]
    pagination_class=CustomLimitOffSetPagination
    
class StudentRetUpdDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    