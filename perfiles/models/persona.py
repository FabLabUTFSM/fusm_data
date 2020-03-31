from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from .tipos import TipoGenero
from uuid import uuid4
from tools.base import CreatedModifiedModel


def profile_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    name = instance.id if instance.id else uuid4()
    return 'personas/{0}.{1}'.format(name, ext)


class Persona(CreatedModifiedModel):
    """
    Toda persona en la base de datos corresponde a una entidad Persona.
    Contiene información común para la identificación. Al momento de su
    ingreso se crea un perfil USM o un perfil profesional.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='la cuenta de usuario con nombre, correo y contraseña'
    )

    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)

    rut = models.CharField(
        'RUT', 
        max_length=12, 
        help_text='el número en su documento de identificación nacional o pasaporte'
    )

    telefono = models.CharField(
        'teléfono',
        max_length=12,
        null=True,
        blank= True,
        help_text='número de contacto personal, ingrese el código de país como +56 en caso de Chile'
    )

    foto = models.ImageField(
        'foto',
        null=True,
        blank=True,
        upload_to=profile_picture_path,
        help_text='foto personal para identificación, debe mostrar el rostro con claridad'
    )

    genero = models.ForeignKey(
        TipoGenero,
        related_name='personas',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='para motivos estadísticos, dejar en blanco si es que no desea especificar'
    )

    fecha_nacimiento = models.DateField(
        'fecha de nacimiento',
        null=True,
        blank=True,
    )

    metadata = JSONField(
        null=True,
        blank=True,
        help_text='información estructurada adicional'
    )

    def get_full_name(self):
        return f'{self.nombres} {self.apellidos}'

    def __str__(self):
        return self.get_full_name()