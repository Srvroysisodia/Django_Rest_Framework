from django.shortcuts import render
from database.models import Student_Details
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your Funtion Based views here.
########################GET METHOD ######################################################################
@api_view()
def stulist(request):
    if request.method=='GET':
        data=Student_Details.objects.all()
        serializer=StudentSerializers(data,many=True)
        return Response (serializer.data)
    
########################POST METHOD ######################################################################
@api_view(['POST'])
def stucreate(request):
    if request.method=="POST":
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'data created!'}
            return Response(msg,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
########################GET/ POST METHOD ###########################################################
@api_view(['GET','POST'])
def stulistpost(request):
    if request.method=='GET':
        data=Student_Details.objects.all()
        serializer=StudentSerializers(data,many=True)
        return Response(serializer.data)
    
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='POST':
        serializer(StudentSerializers(data=request.data))
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Data Created !'}
            return Response(msg)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
#################################### CRUD METHOD #####################################################
@api_view(['GET','POST','PUT','DELETE'])
def crud_fxn(request,pk=None):
    if request.method =='GET':
        id =pk
        if id is not None:
            data=Student_Details.objects.get(pk=id)
            serializer=StudentSerializers(data)
            return Response(serializer.data)
        
        data=Student_Details.objects.all()
        serializer=StudentSerializers(data,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"})
        return Response(serializer.errors)
        
        
    if request.method=='PUT':
        id = pk
        stu=Student_Details.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated"})
        return Response(serializer.errors)
        
    if request.method=='DELETE':
        id = pk
        data=Student_Details.objects.get(pk=id)
        data.delete()
        return Response({"msg":"Data Deleted"})
        
        
        
        
        
        
            