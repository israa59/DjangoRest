from django.shortcuts import render
from rest_framework import response, status
from for_serializer.models import Student
from for_serializer.serializers import StudentSerializer
from rest_framework.decorators import api_view

@api_view(['GET', "POST"])
def student_list(request):
     
     if request.method == 'GET':
          students = Student.objects.all()
          serializer = StudentSerializer(students, many=True)
          return response.Response(serializer.data)
     
     elif request.method == 'POST':
          serializer = StudentSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return response.Response(serializer.data, status= status.HTTP_201_CREATED)
          return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
@api_view(['GET', 'PUT', 'DELETE'])
def student_pk(request,pk):
     
    try:
          student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
         return response.Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
         serializer = StudentSerializer(student)
         return response.Response(serializer.data)
    elif request.method == 'PUT':
         serializer = StudentSerializer(student,data=request.data)
         if serializer.is_valid():
              serializer.save()
              return response.Response(serializer.data)
         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         student.delete()
         return response.Response(status=status.HTTP_204_NO_CONTENT)
     

