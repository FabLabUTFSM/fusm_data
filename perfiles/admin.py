from django.contrib import admin
from .models import Persona, PerfilProfesional, PerfilUSM, TipoActividad, TipoCampus, TipoCarrera, TipoGenero, TipoUnidad

@admin.register(Persona, PerfilProfesional, PerfilUSM)
class PersonaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            if getattr(obj, 'usuario', False):
                return ['usuario',]
            if getattr(obj, 'persona', False):
                return ['persona',]
        else:
            return []

admin.site.register((TipoActividad, TipoCampus, TipoCarrera, TipoGenero, TipoUnidad))