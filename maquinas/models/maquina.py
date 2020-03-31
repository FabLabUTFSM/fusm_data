from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import JSONField
from uuid import uuid4
from .tipos import TipoClasificacion
from tools.base import CreatedModifiedModel

def machine_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    clase_maquina = slugify(instance.nombre)
    return 'maquinas/{0}/imagen.{2}'.format(clase_maquina, ext)


class ClaseMaquina(CreatedModifiedModel):
    """
    Describe un conjunto de máquinas que comparten características.
    Por ejemplo, "Ultimaker 3", o "LaserPro X252"
    """

    clasificacion = models.ForeignKey(
        TipoClasificacion,
        related_name='clases_de_maquina',
        on_delete=models.PROTECT
    )

    nombre = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)

    link_manual = models.URLField(
        'link al manual',
        null=True,
        blank=True,
        help_text='preferentemente una versión PDF del manual'
    )

    nombre_soporte = models.CharField(
        'nombre del soporte',
        max_length=255,
        null=True,
        blank=True,
        help_text='nombre de la persona o empresa a contactar'
    )

    email_soporte = models.EmailField('correo de soporte')

    telefono_soporte = models.CharField(
        'teléfono de soporte',
        max_length=12,
        null=True,
        blank=True,
        help_text='use el código de país, como +569...'
    )

    factor_dificultad = models.SmallIntegerField(
        'factor de dificultad',
        default=1,
        help_text='entre más alto, la máquina es más difícil de usar'
    )

    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to=machine_picture_path
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'clase de máquina'
        verbose_name_plural = 'clases de máquina'

class Maquina(CreatedModifiedModel):
    """
    Describe una máquina en particular.
    Por ejemplo, "Impresora 3D 1"
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    clase_maquina = models.ForeignKey(
        'ClaseMaquina',
        related_name='maquinas',
        on_delete=models.PROTECT
    )

    nombre = models.CharField(max_length=255)

    serie = models.CharField(
        'número de serie',
        max_length=255,
        null=True,
        blank=True,
        help_text='identificador único de la máquina'
    )

    fecha_instalacion = models.DateField('fecha de instalación')

    fecha_retiro = models.DateField(
        'fecha de retiro',
        null=True,
        blank=True,
        help_text=('una máquina retirada no aparece en la lista de máquinas'
                   'activas')
    )
    
    metadata = JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.clase_maquina} - {self.nombre}'

    class Meta:
        verbose_name = 'máquina'
