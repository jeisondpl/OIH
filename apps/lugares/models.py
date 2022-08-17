from django.db import models

class Lugares(models.Model):
	id = models.AutoField(primary_key=True, blank = False, verbose_name = 'idCategoria',
    unique=True)
	pais=models.CharField(blank = False, max_length=20, verbose_name = 'País',null=True)
	departamento=models.CharField(blank = False, max_length=20, verbose_name = 'Departamento',null=True)
	ciudad=models.CharField(blank = False, max_length=20, verbose_name = 'Ciudad',null=True)
	nombreLugar=models.CharField(blank = False, max_length=20, verbose_name = 'Nombre del lugar',null=True)
		
	class Meta:
		verbose_name = 'Lugar'
		verbose_name_plural = 'lugares'
			
	def __str__(self):
		return self.nombreLugar
