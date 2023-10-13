from django.shortcuts import render
from .models import StudentC
from .serializers import StudentCSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class StudentCList(APIView):
    def get(self,request):
        student = StudentC.objects.all()
        serializer = StudentCSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentCDetail(APIView):
    def get_object(self,pk):
        try:
            return StudentC.objects.get(pk=pk)
        except StudentC.DoesNotExist:
            raise Http404
        



    
