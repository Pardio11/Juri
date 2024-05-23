from rest_framework import serializers
from .models import Materia_Juridica

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia_Juridica
        fields = '__all__'
