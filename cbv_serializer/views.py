from django.shortcuts import render
from .models import StudentC
from .serializers import StudentCSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins


class StudentCList(generics.ListCreateAPIView):
    queryset = StudentC.objects.all()
    serializer_class = StudentCSerializer

class StudentCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentC.objects.all()
    serializer_class = StudentCSerializer

'''class StudentCList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StudentC.objects.all()
    serializer_class = StudentCSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class StudentCDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = StudentC.objects.all()
    serializer_class = StudentCSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
        

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
    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentCSerializer(student)
        return Response(serializer.data)
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentCSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

    
