from django.db import models
from django.conf import settings
from personas.models import Cliente
from involucrados.models import Actor,Demandado

class Documento_Base(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        abstract = True  # Define el modelo como abstracto para que no se cree una tabla en la base de datos

class Documento_Cliente(Documento_Base):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_cliente_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_cliente_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'documentos_clientes'

class Documento_Cliente_Archivo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion_s3 = models.CharField(max_length=255)
    documento_personal = models.ForeignKey(Documento_Cliente, on_delete=models.PROTECT)
    class Meta:
        db_table = 'documentos_clientes_archivos'
    def __str__(self):
        return self.nombre

class Documento_Actor(Documento_Base):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_actor_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_actor_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'documentos_actores'

class Documento_Actor_Archivo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion_s3 = models.CharField(max_length=255)
    documento_personal = models.ForeignKey(Documento_Actor, on_delete=models.PROTECT)
    class Meta:
        db_table = 'documentos_actores_archivos'
    def __str__(self):
        return self.nombre
    
class Documento_Demandado(Documento_Base):
    Demandado = models.ForeignKey(Demandado, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_demandado_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documentos_demandado_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'documentos_demandados'

class Documento_Demandado_Archivo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion_s3 = models.CharField(max_length=255)
    documento_personal = models.ForeignKey(Documento_Demandado, on_delete=models.PROTECT)
    class Meta:
        db_table = 'documentos_demandados_archivos'
    def __str__(self):
        return self.nombre