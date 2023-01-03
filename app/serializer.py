from rest_framework import serializers, viewsets
from .models import Temperature


class Dht11serialize(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
