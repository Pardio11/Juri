from rest_framework import serializers
from .models import Cliente, Licenciado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LicenciadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenciado
        fields = '__all__'