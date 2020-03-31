from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_extensions.mixins import DetailSerializerMixin
from django.shortcuts import get_object_or_404
from tools.base import CreatedModifiedViewSet
from .models import (
    Persona, PerfilUSM, PerfilProfesional,
    TipoActividad, TipoCampus, TipoCarrera, TipoGenero, TipoUnidad
)
from .serializers import (
    PersonaSerializer,
    PersonaDetailSerializer,
    PerfilProfesionalSerializer,
    PerfilUSMListSerializer,
    PerfilUSMDetailSerializer,
    TipoActividadSerializer,
    TipoCampusSerializer,
    TipoCarreraSerializer,
    TipoGeneroSerializer,
    TipoUnidadSerializer
)


class PersonaViewSet(DetailSerializerMixin, CreatedModifiedViewSet):
    queryset = Persona.objects.select_related(
        'perfilusm', 'perfilprofesional'
    ).all()
    serializer_class = PersonaSerializer
    serializer_detail_class = PersonaDetailSerializer


class PerfilProfesionalViewSet(ModelViewSet):
    serializer_class = PerfilProfesionalSerializer
    queryset = PerfilProfesional.objects.all()


class PerfilUSMViewSet(DetailSerializerMixin, ModelViewSet):
    serializer_class = PerfilUSMListSerializer
    serializer_detail_class = PerfilUSMDetailSerializer
    queryset = PerfilUSM.objects.all()


class TipoActividadViewSet(ModelViewSet):
    serializer_class = TipoActividadSerializer
    queryset = TipoActividad.objects.all()


class TipoCampusViewSet(ModelViewSet):
    serializer_class = TipoCampusSerializer
    queryset = TipoCampus.objects.all()


class TipoCarreraViewSet(ModelViewSet):
    serializer_class = TipoCarreraSerializer
    queryset = TipoCarrera.objects.all()


class TipoGeneroViewSet(ModelViewSet):
    serializer_class = TipoGeneroSerializer
    queryset = TipoGenero.objects.all()


class TipoUnidadViewSet(ModelViewSet):
    serializer_class = TipoUnidadSerializer
    queryset = TipoUnidad.objects.all()
