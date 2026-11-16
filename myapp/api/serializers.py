from rest_framework import serializers
from myapp import models

class StudentListCreateAPIView(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields="__all__"