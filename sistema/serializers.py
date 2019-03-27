from rest_framework import serializers
from .models import Consumo, Sala, Predio, Estabelecimento


class EstabelecimentoSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Estabelecimento
        fields = ('id', 'user', 'nome', 'slug')
        read_only_fields = ('id', 'slug')


class PredioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Predio
        fields = ('id', 'estabelecimento', 'nome', 'slug')
        read_only_fields = ('id', 'slug')


class ConsumoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumo
        fields = ('id', 'estabelecimento', 'predio', 'sala', 'slug', 'kwh')
        read_only_fields = ('id', 'slug')


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = ('id', 'estabelecimento', 'predio', 'nome')
        read_only_fields = ('id', 'slug')
