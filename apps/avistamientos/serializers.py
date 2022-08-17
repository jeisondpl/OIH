from rest_framework import serializers
from .models import Avistamientos
from apps.lugares.serializers import LugaresSerializer
from apps.especies.serializers import EspecieSerializer


class AvistamientosSerializer(serializers.ModelSerializer):     
    # lugar= LugaresSerializer (many=False, read_only=True)
    # especie= EspecieSerializer (many=False, read_only=True)
    class Meta:
        model = Avistamientos
        fields = ("id","latitud","longitud","autor","notas","lugar","especie")