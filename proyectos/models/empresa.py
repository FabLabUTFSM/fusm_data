from django.db import models
from uuid import uuid4
from tools.base import CreatedModifiedModel


def company_logo_path(instance, filename):
    ext = filename.split('.')[-1]
    name = instance.id if instance.id else uuid4()
    return 'empresas/{0}.{1}'.format(name, ext)


class Empresa(CreatedModifiedModel):
    """
    Describe una compañía asociada a FabLab, que podría o no tener miembros
    trabajando en proyectos dentro del laboratorio.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    razon_social = models.CharField('razón social', max_length=255)
    rut = models.CharField('RUT', max_length=12, null=True, blank=True)

    email = models.EmailField(
        'correo electrónico',
        null=True,
        blank=True,
        help_text=('corresponde al correo electrónico de contacto o '
                   'informaciones de la empresa')
    )

    direccion = models.TextField(
        'dirección', 
        null=True, 
        blank=True,
        help_text='ubicación de la casa matriz'
    )

    giro = models.CharField(
        'giro',
        max_length=255,
        null=True,
        blank=True,
        help_text='definido por el SII'
    )

    logo = models.ImageField(
        'logo',
        null=True,
        blank=True,
        upload_to=company_logo_path
    )

    def __str__(self):
        return f'{self.razon_social}'
    