from rest_framework import serializers
from .models import Mapping1

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping1
        fields = ("src", "dest")
        