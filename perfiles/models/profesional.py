from django.db import models
from .persona import Persona


class PerfilProfesional(models.Model):
    """
    Personas externas al FabLab pero que participan en él tienen asociado este
    perfil. La asociación con Persona es 1-a-1. La persona podría no tener
    asociado un perfil profesional.
    """

    persona = models.OneToOneField(
        Persona, primary_key=True,
        on_delete=models.CASCADE
    )

    empresa = models.ForeignKey(
        'proyectos.Empresa',
        related_name='perfiles_profesionales',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    cargo = models.CharField(
        'cargo',
        max_length=255,
        null=True,
        blank=True,
        help_text='posición que tiene dentro de la empresa o a qué se dedica'
    )

    class Meta:
        verbose_name_plural = 'perfiles profesionales'
