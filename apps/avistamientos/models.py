from django.db import models

from apps.especies.models import Especie
from apps.lugares.models import Lugares


class Avistamientos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name = 'idCategoria', unique=True)
    latitud=models.CharField(blank = False, max_length=20, verbose_name = 'Latitud',null=True)
    longitud=models.CharField(blank = False, max_length=20, verbose_name = 'Longitud',null=True)
    autor=models.CharField(blank = False, max_length=20, verbose_name = 'Autor',null=True)
    notas=models.CharField(blank = False, max_length=20, verbose_name = 'Notas',null=True)
    lugar= models.ForeignKey(Lugares, on_delete=models.CASCADE, verbose_name = 'Lugar', null=True)
    especie= models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name = 'Especie', null=True)
    
    class Meta:
        verbose_name = 'avistamiento'
        verbose_name_plural = 'avistamientos'
        
    def __str__(self):
        return self.autor
