from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user
    
    class Meta:
        model = Usuario
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}