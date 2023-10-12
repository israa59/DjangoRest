from django.shortcuts import render
from rest_framework import response
from for_serializer.models import Student
from for_serializer.serializers import StudentSerializer

def student_request(request):
     
     if request.method == 'GET':
          students = Student.objects.all()
          serializer = StudentSerializer(students, many=True)
          return response.Response(serializer.data)
