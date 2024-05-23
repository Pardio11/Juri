from rest_framework import serializers
from .models import Tipo_Juicio, Estado_Procesal, Estado_Procesal_Historial, Archivo_Personal

class TipoJuicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Juicio
        fields = '__all__'
        
class EstadoProcesalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Procesal
        fields = '__all__'

class EPHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Procesal_Historial
        fields = '__all__'

class APSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo_Personal
        fields = '__all__'