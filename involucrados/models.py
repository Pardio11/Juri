from django.db import models
from personas.models import Persona
from archivos_personales.models import Archivo_Personal


class Actor(Persona):
    archivo_personal = models.ForeignKey(Archivo_Personal, related_name='actores', on_delete=models.CASCADE)
    class Meta:
        db_table = 'actores'

class Demandado(Persona):
    archivo_personal = models.ForeignKey(Archivo_Personal, related_name='demandados', on_delete=models.CASCADE)
    class Meta:
        db_table = 'demandados'


