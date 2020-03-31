from django.db import models
from tools.base import CategoryModel

class TipoClasificacion(CategoryModel):
    """
    Lista de los diferentes tipos de equipamiento con los que cuenta el
    laboratorio. Corresponde a una descripción general de lo que hace el
    equipo.

    Por ejemplo, "Impresora 3D", "Cortadora Láser", etc.
    """
    descripcion = models.TextField('descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'clasificación'
        verbose_name_plural = 'clasificaciones'