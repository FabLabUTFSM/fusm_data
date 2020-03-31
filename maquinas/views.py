from rest_framework.viewsets import ModelViewSet
from tools.base import CreatedModifiedViewSet
from .models import (
    Mantenimiento,
    TareaMantenimiento,
    Maquina,
    ClaseMaquina,
    TipoClasificacion
)

from .serializers import (
    MaquinaSerializer,
    ClaseMaquinaSerializer,
    MantenimientoSerializer,
    TareaMantenimientoSerializer,
    TipoClasificacionSerializer
)


class MantenimientoViewSet(ModelViewSet):
    serializer_class = MantenimientoSerializer
    queryset = Mantenimiento.objects.all()


class TareaMantenimientoViewSet(CreatedModifiedViewSet):
    serializer_class = TareaMantenimientoSerializer
    queryset = TareaMantenimiento.objects.all()


class ClaseMaquinaViewSet(CreatedModifiedViewSet):
    serializer_class = ClaseMaquinaSerializer
    queryset = ClaseMaquina.objects.all()


class MaquinaViewSet(CreatedModifiedViewSet):
    serializer_class = MaquinaSerializer
    queryset = Maquina.objects.all()


class TipoClasificacionViewSet(ModelViewSet):
    serializer_class = TipoClasificacionSerializer
    queryset = TipoClasificacion.objects.all()