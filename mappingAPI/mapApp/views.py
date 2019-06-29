from django.shortcuts import render
from rest_framework import generics
from .models import Mapping1
from .serializers import MappingSerializer

class listMappingsView(generics.ListAPIView):
    queryset = Mapping1.objects.all()
    serializer_class = MappingSerializer