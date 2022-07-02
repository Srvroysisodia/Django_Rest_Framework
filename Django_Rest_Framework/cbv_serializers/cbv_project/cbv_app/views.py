from rest_framework import generics

from cbv_app.models import stu_model
from cbv_app.serializers import serial

class Student_list(generics.ListCreateAPIView,):
    queryset = stu_model.objects.all()
    serializer_class = serial

class Student_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = stu_model.objects.all()
    serializer_class = serial



'''
from .models import stu_model
from .serializers import serial
from rest_framework import mixins , generics

class Student_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset =  stu_model.objects.all()
    serializer_class = serial

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class Student_details(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin):
     queryset = stu_model.objects.all()
     serializer_class = serial

     def get(self,request,stu_id):
        return self.retrieve(request,stu_id)
     def put(self,request,stu_id):
        return self.update(request,stu_id)
     def delete(self,request,stu_id):
        return self.destroy(request,stu_id)







from django.shortcuts import render
from cbv_app.models import stu_model
from cbv_app.serializers import serial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
class Student_list(APIView):
    def get(self,request):
        Student = stu_model.objects.all()
        serializers = serial(Student,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializer = serial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Student_details(APIView):
    def get_object(self,stu_id):
        try:
            return stu_model.objects.get(pk=stu_id)

        except stu_model.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)

    def get(self,request,stu_id):
        student = self.get_object(stu_id)
        s = serial(student)
        return Response(s.data)
    def put(self,request,stu_id):
        student = self.get_object(stu_id)
        s = serial(s,data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,stu_id):
        s =  self.get_object(stu_id)
        s.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
        '''
