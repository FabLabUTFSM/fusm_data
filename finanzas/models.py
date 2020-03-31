from django.db import models
from uuid import uuid4
from tools.base import CreatedModifiedModel, CategoryModel


class Unidad(models.TextChoices):
    VECES = 'V', 'Veces'
    SEGUNDOS = 'S', 'Segundos'
    MINUTOS = 'M', 'Minutos'
    HORAS = 'H', 'Horas',
    BLOQUES = 'B', 'Bloques'
    DIAS = 'D', 'Días'


class TipoCategoria(CategoryModel):
    """
    La categoría de un servicio. Es un modo de agrupar varios servicios.
    """

    class Meta:
        verbose_name = 'categoría'


class Servicio(CreatedModifiedModel):
    """
    Describe el costo de usar alguna parte del equipamiento o el espacio del
    laboratorio, el costo se calcula a partir de un factor relacionado con el
    tipo de usuario, por lo tanto el valor que representa este modelo es solo
    el valor base (factor 1).
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    item = models.PositiveSmallIntegerField('ítem')
    costo = models.PositiveIntegerField(default=0)
    
    activo = models.BooleanField(
        default=True,
        help_text='un servicio inactivo no aparece en la lista de servicios'
    )

    unidad = models.CharField(
        max_length=1,
        choices=Unidad.choices,
        default='M',
        help_text='indica bajo qué periodo se hace el cobro'
    )

    categoria = models.ForeignKey(
        TipoCategoria,
        verbose_name='categoría',
        related_name='servicios',
        on_delete=models.PROTECT
    )
    
