from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import JSONField
from uuid import uuid4
from tools.base import CreatedModifiedModel
from .tipos import TipoMaterial


def work_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    name = instance.id if instance.id else uuid4()
    clase_maquina = slugify(instance.maquina.clase_maquina.nombre)
    return 'trabajos/{0}/{1}.{2}'.format(clase_maquina, name, ext)


class Trabajo(CreatedModifiedModel):
    """
    Describe el uso de una de las máquinas del laboratorio por una persona
    capacitada. La entrada se crea cuando el trabajo comienza y puede
    modificarse cuando el trabajo termina.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    maquina = models.ForeignKey(
        'maquinas.Maquina',
        verbose_name='máquina',
        related_name='trabajos',
        on_delete=models.PROTECT,
        help_text='la máquina donde se realizó el trabajo'
    )

    operador = models.ForeignKey(
        'perfiles.Persona',
        related_name='trabajos',
        on_delete=models.PROTECT,
        help_text=('la persona que operó la máquina durante la realización '
                   'de la tarea')
    )

    solicitado_por = models.ForeignKey(
        'perfiles.Persona',
        related_name='trabajos_solicitados',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text=('seleccionar si es que este trabajo fue solicitado por '
                   'una persona distinta a la que operó la máquina')
    )

    fecha_inicio = models.DateTimeField('inicio')
    
    fecha_termino = models.DateTimeField(
        'término',
        null=True,
        blank=True,
        help_text='puede especificarte cuando termine la tarea'
    )

    material = models.ForeignKey(
        TipoMaterial,
        verbose_name='material',
        related_name='trabajos',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    cantidad_material = models.CharField(
        'cantidad de material',
        max_length=64,
        null=True,
        blank=True,
        help_text=('indica la cantidad de material en la unidad indicada por '
                   'el tipo seleccionado')
    )

    material_fablab = models.BooleanField(
        'material de FabLab',
        default=True,
        help_text='marcar si el material pertenece al laboratorio'
    )

    foto = models.ImageField(
        null=True,
        blank=True,
        help_text='una imagen que muestra el trabajo realizado',
        upload_to=work_picture_path
    )

    comentarios = models.TextField(null=True, blank=True)
    metadata = JSONField(null=True, blank=True)
