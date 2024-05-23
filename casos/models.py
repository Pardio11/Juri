from django.db import models
from django.conf import settings
from personas.models import Licenciado,Cliente

class Caso(models.Model):
    nombre = models.CharField(max_length= 100, unique=True)
    descripcion = models.TextField(blank=True)
    cotizacion = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    licenciados = models.ManyToManyField(Licenciado)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='casos_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='casos_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'casos'
    def __str__(self):
        return self.nombre