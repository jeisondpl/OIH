from django.shortcuts import render

# Create your views here.
from .serializers import LugaresSerializer
from .models import Lugares

from rest_framework.generics import (ListCreateAPIView, DestroyAPIView,UpdateAPIView)


class LugaresList(ListCreateAPIView):
    queryset = Lugares.objects.all()
    serializer_class = LugaresSerializer

class LugaresDestroy(DestroyAPIView):
    queryset = Lugares.objects.all()
    serializer_class = LugaresSerializer

class LugaresUpdate(UpdateAPIView):
    queryset = Lugares.objects.all()
    serializer_class = LugaresSerializer
