from rest_framework.views import APIView
from rest_framework.response import Response
from myapp import models
from . import serializers
from rest_framework import generics, mixins


class StudentListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentListCreateAPIView
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    


    

class StudentRetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentListCreateAPIView
    lookup_field= "id"
    lookup_url_kwarg= "id"


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)