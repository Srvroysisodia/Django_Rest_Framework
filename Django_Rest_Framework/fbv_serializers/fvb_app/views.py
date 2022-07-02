from fvb_app.models import studentTable
from fvb_app.serializer import serial
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def stu_list(request):
    if request.method == 'GET':
        student = studentTable.objects.all()
        serializers = serial(student,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = serial(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def stu_detail(request,pk):
    try:
        students = studentTable.objects.get(pk=pk)
    except studentTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=serial(students)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer=serial(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)