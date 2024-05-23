from rest_framework import serializers
from .models import Demandado,Actor

class DemandadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demandado
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'