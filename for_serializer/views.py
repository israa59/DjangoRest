from django.shortcuts import render
from rest_framework import response, status
from for_serializer.models import Student
from for_serializer.serializers import StudentSerializer

def student_request(request):
     
     if request.method == 'GET':
          students = Student.objects.all()
          serializer = StudentSerializer(students, many=True)
          return response.Response(serializer.data)
     
     elif request.method == 'POST':
          serializer = StudentSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return response.Response(serializer, status= status.HTTP_201_CREATED)
          return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
