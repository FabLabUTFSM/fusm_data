from django.contrib import admin
from .models import Trabajo, TipoMaterial, Contexto

# Register your models here.
admin.site.register((Trabajo, TipoMaterial, Contexto))
