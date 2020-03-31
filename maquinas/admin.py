from django.contrib import admin
from .models import TareaMantenimiento, TipoClasificacion, Mantenimiento, Maquina, ClaseMaquina

# Register your models here.
admin.site.register((TareaMantenimiento, TipoClasificacion, Mantenimiento, Maquina, ClaseMaquina))