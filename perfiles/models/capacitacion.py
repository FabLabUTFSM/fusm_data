from django.db import models
from uuid import uuid4
from .persona import Persona
from tools.base import CreatedModifiedModel


class Capacitacion(CreatedModifiedModel):
    """
    Describe una autorización para la utilización de una clase de máquina en
    el laboratorio. Una persona puede tener múltiples capacitaciones.
    La relación con el capacitador es opcional ya que no se tiene información
    de todas las capacitaciones.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    persona = models.ForeignKey(
        Persona,
        related_name='capacitaciones',
        on_delete=models.CASCADE,
        help_text='el perfil de la persona capacitada'
    )

    capacitador = models.ForeignKey(
        Persona,
        related_name='capacitador_de',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='la persona que realizó la capacitación'
    )

    clase_maquina = models.ForeignKey(
        'maquinas.ClaseMaquina',
        verbose_name='clase de máquina',
        related_name='capacitaciones',
        on_delete=models.CASCADE,
        help_text='la clase de equipamiento sobre la que se capacitó'
    )

    fecha = models.DateField(
        help_text=('la fecha en que se realizó. en caso de que haya durado más '
                   'de una sesión, la fecha de la sesión final')
    )

    class Meta:
        verbose_name = 'capacitación'
        verbose_name_plural = 'capacitaciones'
