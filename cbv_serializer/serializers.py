from rest_framework import serializers
from .models import StudentC

class StudentCSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentC
        fields = ['name', 'score']