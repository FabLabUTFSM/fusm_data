from django.db import models
from tools.base import CategoryModel

class TipoGenero(CategoryModel):
    """
    Lista los géneros disponibles de una persona.
    """

    class Meta:
        verbose_name = 'género'


class Region(models.TextChoices):
    AI = 'AI', 'Aisén del General Carlos Ibañez del Campo'
    AN = 'AN', 'Antofagasta'
    AP = 'AP', 'Arica y Parinacota'
    AR = 'AR', 'La Araucanía'
    AT = 'AT', 'Atacama'
    BI = 'BI', 'Biobío'
    CO = 'CO', 'Coquimbo'
    LI = 'LI', 'Libertador General Bernardo O\'Higgins'
    LL = 'LL', 'Los Lagos'
    LR = 'LR', 'Los Ríos'
    MA = 'MA', 'Magallanes'
    ML = 'ML', 'Maule'
    NB = 'NB', 'Ñuble'
    RM = 'RM', 'Región Metropolitana de Santiago'
    TA = 'TA', 'Tarapacá'
    VS = 'VS', 'Valparaíso'


class TipoCampus(CategoryModel):
    """
    Lista de los campus de la universidad. Permite agrupar a los alumnos por
    región.
    """

    region = models.CharField(
        'región',
        max_length=2,
        choices=Region.choices,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'campus'
        verbose_name_plural = 'campus'


class TipoActividad(CategoryModel):
    """
    Lista de las actividades con las que puede estar asociada una persona en
    la USM.
    """

    descripcion = models.TextField('descripción', null=True, blank=True)

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'


class TipoUnidad(CategoryModel):
    """
    Lista de las unidades en las que puede estar asociado un miembro de la
    comunidad universitaria en la USM.
    """

    class Meta:
        verbose_name = 'unidad'
        verbose_name_plural = 'unidades'


class TipoCarrera(CategoryModel):
    """
    Lista de las carreras con las que puede estar asociado un estudiante
    en la USM.
    """

    class Meta:
        verbose_name = 'carrera'
