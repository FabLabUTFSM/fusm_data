from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from .maquina import ClaseMaquina, Maquina
from tools.base import CreatedModifiedModel

def task_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    name = instance.id if instance.id else uuid4()
    clase_maquina = slugify(instance.clase_maquina.nombre)
    return 'maquinas/{0}/tareas/{1}.{2}'.format(clase_maquina, name, ext)

PERIOD_CHOICES = (
    ('H', 'Horas'),
    ('D', 'Días'),
    ('S', 'Semanas'),
    ('M', 'Meses'),
    ('E', 'Semestres'),
    ('A', 'Años')
)

class TareaMantenimiento(CreatedModifiedModel):
    """
    Lista las tareas de mantenimiento que se le tienen que hacer a una clase
    de máquina en particular. Un set de tareas de mantenimiento corresponde
    al plan de mantenimiento de una máquina.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    clase_maquina = models.ForeignKey(
        ClaseMaquina,
        verbose_name='clase de máquina',
        related_name='plan_de_mantenimiento',
        on_delete=models.CASCADE,
    )
    
    titulo = models.CharField('título', max_length=255)
    descripcion = models.TextField('descripción', null=True, blank=True)

    imagen = models.ImageField(
        null=True,
        blank=True,
        help_text='imagen que ayude a describir la tarea a realizar',
        upload_to=task_picture_path
    )

    prioridad = models.PositiveSmallIntegerField(
        help_text='números más bajos van primero'
    )

    frecuencia = models.PositiveSmallIntegerField(
        help_text='cantidad de periodos con la que debería realizarse la tarea'
    )

    periodo = models.CharField(
        max_length=1,
        default='D',
        choices=PERIOD_CHOICES,
        help_text='periodicidad con que debería realizarse la tarea'
    )

    class Meta:
        verbose_name = 'tarea de mantenimiento'
        verbose_name_plural = 'tareas de mantenimiento'


class Mantenimiento(models.Model):
    """
    Corresponde a una tarea de mantenimiento realizada por un miembro del
    personal, indicando qué tarea fue, en qué máquina y cuándo fue realizada.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    tarea = models.ForeignKey(
        TareaMantenimiento,
        related_name='mantenimientos',
        on_delete=models.CASCADE
    )

    maquina = models.ForeignKey(
        Maquina,
        verbose_name='máquina',
        related_name='mantenimientos',
        on_delete=models.CASCADE
    )

    realizado_por = models.ForeignKey(
        'perfiles.Persona',
        related_name='mantenimientos',
        on_delete=models.CASCADE,
        help_text='la persona que realizó la tarea'
    )

    fecha = models.DateTimeField(
        help_text='el momento en que se realizó la tarea'
    )
    
    comentario = models.TextField(null=True, blank=True)
