from django.db import models

class Materia_Juridica(models.Model):
    nombre = models.CharField(max_length = 60)
    class Meta:
        db_table = 'materias_juridicas'
    def __str__(self):
        return self.nombre