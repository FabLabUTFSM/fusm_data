from django.db import models
from tools.base import CategoryModel

class TipoMaterial(CategoryModel):
    """
    Describe los tipos de materiales utilizables en las máquinas
    """

    unidad = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        help_text=('indica la unidad con la que debería medirse el material.'
                   'ej. "g", "cm^2"')
    )

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiales'