from rest_framework import serializers
from .models import Cita,Tipo_Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
        
class TipoCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Cita
        fields = '__all__'