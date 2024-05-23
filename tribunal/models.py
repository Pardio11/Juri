from django.db import models
from materias.models import Materia_Juridica
class Distrito(models.Model):
    nombre = models.CharField(max_length = 80)
    class Meta:
        db_table = 'distrito'
    def __str__(self):
        return self.nombre


class Juzgado_Sala(models.Model):
    nombre = models.CharField(max_length = 80)
    materia_juridica = models.ForeignKey(Materia_Juridica, on_delete=models.PROTECT)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    class Meta:
        db_table = 'juzgados_salas'
    def __str__(self):
        return self.nombre
