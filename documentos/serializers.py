from rest_framework import serializers
from .models import Documento_Cliente

class DocumentoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento_Cliente
        fields = '__all__'