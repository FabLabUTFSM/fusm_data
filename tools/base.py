from django.db import models
from django.conf import settings
from rest_framework import serializers, viewsets

class CreatedModifiedModel(models.Model):
    fecha_creacion = models.DateTimeField('fecha de creación', auto_now_add=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_creadas', on_delete=models.PROTECT)
    fecha_modificacion = models.DateTimeField('fecha de modificación', auto_now=True)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modificadas', on_delete=models.PROTECT)

    class Meta:
        abstract = True


class CategoryModel(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True


class CreatedModifiedModelSerializer(serializers.ModelSerializer):
    creado_por = serializers.HyperlinkedRelatedField(read_only=True, view_name='usuario-detail')
    modificado_por = serializers.HyperlinkedRelatedField(read_only=True, view_name='usuario-detail')


class CreatedModifiedViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(creado_por=req.user, modificado_por=req.user)

    def perform_update(self, serializer):
        req = serializer.context['request']
        serializer.save(modificado_por=req.user)