from rest_framework import serializers
from .models import Consumo, Sala

class ConsumoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Consumo
        fields = ('id', 'predio', 'sala', 'sala', 'slug', 'kwh', 'data')
        read_only_fields = ('id', 'slug')


class SalaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Sala
        fields = ('id', 'predio', 'nome', 'slug')
        read_only_fields = ('id', 'slug')
