from django.db import models

# Create your models here.

# Create your models here.





class CategoriasTaxonomicas(models.Model):
	id = models.AutoField(primary_key=True,  verbose_name = 'idCategoria',unique=True)
	reino=models.CharField(blank = False, max_length=20, verbose_name = 'Reino',null=True)
	filo=models.CharField(blank = False, max_length=20, verbose_name = 'Filo',null=True)
	clase=models.CharField(blank = False, max_length=20, verbose_name = 'Clase',null=True)
	orden=models.CharField(blank = False, max_length=20, verbose_name = 'Orden',null=True)
	familia=models.CharField(blank = False, max_length=20, verbose_name = 'Familia',null=True)
	genero=models.CharField(blank = False, max_length=20, verbose_name = 'Genero',null=True)
	

	class Meta:
		verbose_name = 'Categoria_Taxonomica'
		verbose_name_plural = 'Categorias_Taxonomicas'
			
	def __str__(self):
		return str(self.id)
		

class Especie(models.Model):
	id = models.AutoField(primary_key=True,  verbose_name = 'idEspecie',unique=True)
	nombre_comun = models.CharField(blank = False, max_length=20, verbose_name = 'Nombre_Comun',null=True)
	nombre_cientifico  = models.CharField(blank = False, max_length=20, verbose_name = 'Nombre_Cientifico', null=True)
	categoria= models.ForeignKey(CategoriasTaxonomicas, on_delete=models.CASCADE, verbose_name = 'Categoria_Taxonomica', null=True)
	# Categorias_taxonomicas = (('0', "Reino"), ('1', "Filo"), ('2', "Clase"),('3', "Orden"),
	# ('4', "Familia"), ('5', "Genero"), ('6', "Especie"))
	# categoria = models.CharField(max_length=20, choices=Categorias_taxonomicas, null=True, blank=True)

	class Meta:
		verbose_name = 'Especie'
		verbose_name_plural = 'Especies'
			
	def __str__(self):
		return self.nombre_comun

