from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import JSONField
from uuid import uuid4
from tools.base import CreatedModifiedModel
from .empresa import Empresa

def team_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    name = slugify(instance.name)
    return 'proyectos/{0}/equipo.{1}'.format(name, ext)

def project_logo_path(instance, filename):
    ext = filename.split('.')[-1]
    name = slugify(instance.name)
    return 'proyectos/{0}/logo.{1}'.format(name, ext)


class Proyecto(CreatedModifiedModel):
    """
    Describe un proyecto conformado por uno o más personas.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=255)

    descripcion_corta = models.CharField(
        max_length=150,
        help_text='describe al proyecto en un tweet'
    )

    descripcion = models.TextField('descripción')
    fecha_ingreso = models.DateField('fecha de ingreso')

    fecha_retiro = models.DateField(
        'fecha de retiro',
        null=True,
        blank=True,
        help_text='un proyecto retirado no aparece entre los proyectos actuales'
    )

    sitio_web = models.URLField(blank=True, null=True)
    correo_contacto = models.EmailField('correo de contacto')

    logo = models.ImageField(
        null=True,
        blank=True,
        upload_to=project_logo_path,
        help_text='de preferencia transparente'
    )

    foto_equipo = models.ImageField(
        null=True,
        blank=True,
        upload_to=team_picture_path,
        help_text='foto en donde se muestren a los miembros del equipo'
    )

    empresa = models.ForeignKey(
        Empresa,
        related_name='proyectos',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='si es que el proyecto pertenece a una empresa, indicar a cual'
    )

    miembros = models.ManyToManyField(
        'perfiles.Persona',
        through='MiembroProyecto',
        through_fields=('proyecto', 'persona')
    )

    metadata = JSONField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class MiembroProyecto(CreatedModifiedModel):
    """
    Relaciona una persona con un proyecto. Una persona puede tener asociados
    múltiples proyectos.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    persona = models.ForeignKey('perfiles.Persona', on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField('fecha de ingreso')

    fecha_retiro = models.DateField(
        'fecha de retiro',
        null=True,
        blank=True,
        help_text='un miembro retirado no aparece en la lista de integrantes'
    )

    cargo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='describe el rol que tiene el integrante en el proyecto'
    )

    es_encargado = models.BooleanField(
        default=False,
        help_text='marcar si el integrante sirve como contacto responsable'
    )

    def __str__(self):
        return f'{self.persona} ({self.proyecto})'