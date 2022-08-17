from rest_framework import serializers
from .models import Especie, CategoriasTaxonomicas


class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ("__all__")


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasTaxonomicas
        fields = ("__all__")