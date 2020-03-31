from django.contrib.auth import get_user_model
from rest_framework import serializers
from tools.base import CreatedModifiedModelSerializer
from .models import (
    Persona, PerfilUSM, PerfilProfesional,
    TipoActividad, TipoCampus, TipoCarrera, TipoGenero, TipoUnidad
)
from proyectos.models import Empresa

Usuario = get_user_model()


class PersonaNestedSerializer(serializers.ModelSerializer):
    persona = serializers.HyperlinkedIdentityField(view_name='persona-detail')
    email = serializers.EmailField(source='usuario.email', read_only=True)
    
    class Meta:
        model = Persona
        fields = ('persona', 'nombres', 'apellidos', 'email')


class PerfilUSMListSerializer(serializers.ModelSerializer):
    perfil = serializers.HyperlinkedIdentityField(view_name='perfilusm-detail')
    persona = serializers.HyperlinkedRelatedField(queryset=Persona.objects.all(), view_name='persona-detail')
    nombres = serializers.CharField(source='persona.nombres', read_only=True)
    apellidos = serializers.CharField(source='persona.apellidos', read_only=True)

    class Meta:
        model = PerfilUSM
        fields = '__all__'


class PerfilUSMDetailSerializer(serializers.ModelSerializer):
    persona = PersonaNestedSerializer(read_only=True)
    class Meta:
        model = PerfilUSM
        fields = '__all__'


class PerfilUSMNestedSerializer(serializers.ModelSerializer):
    perfil = serializers.HyperlinkedIdentityField(view_name='perfilusm-detail')
    campus = serializers.StringRelatedField(read_only=True)
    actividad = serializers.StringRelatedField(read_only=True)
    unidad = serializers.StringRelatedField(read_only=True)
    carrera = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PerfilUSM
        exclude = ('persona',)


class PerfilProfesionalSerializer(serializers.ModelSerializer):
    perfil = serializers.HyperlinkedIdentityField(view_name='perfilprofesional-detail')
    persona = PersonaNestedSerializer(read_only=True)
    # empresa = serializers.HyperlinkedRelatedField(queryset=Empresa.objects.all(), view_name='empresa-detail')

    class Meta:
        model = PerfilProfesional
        fields = ('perfil', 'persona', 'empresa', 'cargo')


class NestedProfesionalSerializer(PerfilProfesionalSerializer):
    persona = None
    empresa = serializers.StringRelatedField(read_only=True)
    class Meta(PerfilProfesionalSerializer.Meta):
        fields = ('perfil', 'empresa', 'cargo')



class PersonaSerializer(CreatedModifiedModelSerializer):
    persona = serializers.HyperlinkedIdentityField(view_name='persona-detail')
    #usuario = serializers.HyperlinkedRelatedField(queryset=Usuario.objects.all(), view_name='usuario-detail')
    email = serializers.EmailField(source='usuario.email', read_only=True)

    class Meta:
        model = Persona
        fields = '__all__'


class PersonaDetailSerializer(CreatedModifiedModelSerializer):
    usuario = serializers.HyperlinkedRelatedField(view_name='usuario-detail', queryset=Usuario.objects.all())
    email = serializers.EmailField(source='usuario.email', read_only=True)
    perfilprofesional = NestedProfesionalSerializer(read_only=True)
    perfilusm = PerfilUSMNestedSerializer(read_only=True)
    genero = serializers.StringRelatedField()

    class Meta:
        model = Persona
        fields = '__all__'


class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividad
        fields = '__all__'


class TipoCampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCampus
        fields = '__all__'


class TipoCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCarrera
        fields = '__all__'


class TipoGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGenero
        fields = '__all__'


class TipoUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = '__all__'