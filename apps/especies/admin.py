from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Especie, CategoriasTaxonomicas

admin.site.register(Especie)
admin.site.register(CategoriasTaxonomicas)