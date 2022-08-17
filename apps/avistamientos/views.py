from django.shortcuts import render
from .serializers import AvistamientosSerializer
from .models import Avistamientos
from rest_framework.generics import (ListCreateAPIView, DestroyAPIView,UpdateAPIView)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from apps.especies.models import Especie
import hashlib


class AvistamientosList(ListCreateAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer

class AvistamientosDestroy(DestroyAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer

class AvistamientosUpdate(UpdateAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer


# avistamientoForIdEspecie
class avistamientoForIdEspecie(ListCreateAPIView):
    serializer_class = AvistamientosSerializer
    def get_queryset(self):
        idEspecie = self.kwargs['pk']
        especie = Avistamientos.objects.filter(especie=idEspecie)
        return especie

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

@api_view(['GET'])
def findid(request,*args, **kwargs):
    print("---------------",kwargs["categoria"])
    print("---------------",kwargs["id"])

    id_especie = kwargs["id"]
    queryset = Especie.objects.all().values()
    aux = {}
    for doc in queryset:
        if encrypt_string(doc["nombre_comun"]) == id_especie:
            aux = doc
            break
  
    return Response(aux)



@api_view(['GET'])
def list_marine_OIH(request,*args, **kwargs): 
    JsonResponse = {
        "animales": []   
    }
    queryset = Especie.objects.all().values()

    print(queryset)

    base_url= "http://portete.invemar.org.co/chm/api/oih/"
    base_url2= "http://localhost:8000/chm/api/oih/findid/"
    for doc in queryset:
        JsonResponse["animales"].append({
        "name":doc,
        "@id": base_url2 + 'vessel/'+encrypt_string(doc["nombre_comun"]),
        })  

        
        # print(doc["nombre_comun"],">",encrypt_string(doc["nombre_comun"]))
        # JsonResponse = {
        # "@context": {
        # "@vocab": "https://schema.org/"
        # },
        # "name": "Resource collection for https://CHM-LAC/",
       
        # "@id": base_url2 + 'vessel/'+encrypt_string(doc["nombre_comun"]),
        # "@type":[
        #         "ItemList",
        #     ],
        # "author": {
        #     "@id": "",
        #     "@type": "Organization",
        #     "name": "Instituto de Investigaciones Marinas y Costeras INVEMAR",
        #     "sameAs": [
        #         "https://oceanexpert.org/institution/6795"
        #     ]
        # },
        # "itemListOrder": "https://schema.org/ItemListUnordered",
        # "numberOfItems": 0,
        # "itemListElement": []    
        # }

    return Response(JsonResponse)

