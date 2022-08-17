from django.shortcuts import render
from .serializers import EspecieSerializer, CategoriaSerializer
from .models import Especie, CategoriasTaxonomicas
from rest_framework.generics import (ListCreateAPIView, DestroyAPIView, UpdateAPIView)

# Especies
class EspecieList(ListCreateAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class EspecieDestroy(DestroyAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class EspecieUpdate(UpdateAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

# CategoriasTaxonomicas
class CategoriaList(ListCreateAPIView):
    queryset = CategoriasTaxonomicas.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDestroy(DestroyAPIView):
    queryset = CategoriasTaxonomicas.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaUpdate(UpdateAPIView):
    queryset = CategoriasTaxonomicas.objects.all()
    serializer_class = CategoriaSerializer

