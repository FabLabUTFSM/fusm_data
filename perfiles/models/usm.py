from django.db import models
from .persona import Persona
from .tipos import TipoCampus, TipoActividad, TipoUnidad, TipoCarrera

class PerfilUSM(models.Model):
    """
    Personas que corresponden a miembros de la comunidad universitaria tienen
    asociados este perfil. La asociación con Persona es 1-a-1. La persona
    podría no tener asociado un perfil USM (como un miembro externo).
    """

    persona = models.OneToOneField(
        Persona,
        on_delete=models.CASCADE,
        primary_key=True
    )

    campus = models.ForeignKey(
        TipoCampus,
        related_name='perfiles_usm',
        on_delete=models.PROTECT,
        help_text='el campus al que está asociada la persona'
    )

    rol = models.CharField(
        'rol USM',
        max_length=12,
        null=True,
        blank=True,
        help_text='en caso de estudiantes'
    )

    actividad = models.ForeignKey(
        TipoActividad,
        related_name='perfiles_usm',
        on_delete=models.PROTECT,
        help_text='actividad principal que realiza en el campus'
    )

    unidad = models.ForeignKey(
        TipoUnidad,
        related_name='perfiles_usm',
        on_delete=models.PROTECT,
        help_text='la unidad a la que está vinculada'
    )

    carrera = models.ForeignKey(
        TipoCarrera,
        related_name='perfiles_usm',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='en el caso de estar asociados a una carrera'
    )

    ingreso = models.PositiveSmallIntegerField(
        'año de ingreso',
        null=True,
        blank=True,
        help_text='año en que comienza su actividad principal'
    )

    avance = models.PositiveSmallIntegerField(
        'año de avance',
        null=True,
        blank=True,
        help_text='en el caso de estudiantes, el año de su ramo más atrasado'
    )

    prioridad = models.DecimalField(
        'prioridad académica',
        decimal_places=3,
        max_digits=8,
        null=True,
        blank=True,
        help_text='en caso de estudiantes, el valor de su última prioridad'
    )

    def __str__(self):
        return f'{self.persona}'

    class Meta:
        verbose_name = 'perfil USM'
        verbose_name_plural = 'perfiles USM'