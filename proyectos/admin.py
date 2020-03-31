from django.contrib import admin
from .models import Empresa, Proyecto, MiembroProyecto

# Register your models here.
admin.site.register((Empresa, Proyecto, MiembroProyecto))