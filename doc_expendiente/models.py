from django.db import models
from django.conf import settings
from archivos_personales.models import Estado_Procesal_Historial, Subproceso
class Tipo_Auto(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        db_table = 'tipos_auto'
    def __str__(self):
        return self.nombre

class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(Tipo_Auto, on_delete=models.PROTECT)
    historial_ES = models.ForeignKey(Estado_Procesal_Historial, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='auto_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='auto_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'autos'
    def __str__(self):
        return self.nombre
    
class Foja(models.Model):
    enumeracion = models.PositiveSmallIntegerField()
    direccion_s3 = models.CharField(max_length=255)
    auto = models.ForeignKey(Auto, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='foja_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='foja_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'fojas'
    def __str__(self):
        return self.nombre

class Sub_Auto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(Tipo_Auto, on_delete=models.PROTECT)
    subproceso = models.ForeignKey(Subproceso, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sub_auto_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sub_auto_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'sub_autos'
    def __str__(self):
        return self.nombre
    
class Sub_Foja(models.Model):
    enumeracion = models.PositiveSmallIntegerField()
    direccion_s3 = models.CharField(max_length=255)
    sub_auto = models.ForeignKey(Sub_Auto, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sub_foja_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sub_foja_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'sub_fojas'
    def __str__(self):
        return self.nombre