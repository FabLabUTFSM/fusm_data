from rest_framework import serializers
from tools.base import CreatedModifiedModelSerializer
from .models import (
    ClaseMaquina,
    Mantenimiento,
    Maquina,
    TareaMantenimiento,
    TipoClasificacion
)


class ClaseMaquinaSerializer(CreatedModifiedModelSerializer):
    class Meta:
        model = ClaseMaquina
        fields = '__all__'


class NestedClaseMaquinaSerializer(serializers.ModelSerializer):
    clase = serializers.HyperlinkedIdentityField(source='clase_maquina', view_name='clasemaquina-detail')

    class Meta:
        model = ClaseMaquina
        fields = ('clase', 'nombre', 'fabricante', 'foto')


class MaquinaSerializer(CreatedModifiedModelSerializer):
    clase_maquina = NestedClaseMaquinaSerializer(read_only=True)
    class Meta:
        model = Maquina
        fields = '__all__'


class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'


class TareaMantenimientoSerializer(CreatedModifiedModelSerializer):
    class Meta:
        model = TareaMantenimiento
        fields = '__all__'


class TipoClasificacionSerializer(CreatedModifiedModelSerializer):
    class Meta:
        model = TipoClasificacion
        fields = '__all__'