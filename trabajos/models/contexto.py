from django.db import models
from tools.base import CategoryModel
from .trabajo import Trabajo

class Contexto(CategoryModel):
    """
    Contexto funciona como una serie de tags para identificar el motivo
    de cada trabajo.
    """
    
    descripcion = models.TextField(
        'descripción',
        null=True,
        blank=True,
        help_text='explica cuándo tiene que ser utilizado este contexto'
    )

    trabajos = models.ManyToManyField(Trabajo, related_name='contextos')