from django.db import models
from involucrados.models import Actor,Demandado
from django.conf import settings
from archivos_personales.models import Estado_Procesal_Historial

class Tipo_Cita(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Cita(models.Model):
    ubicacion = models.CharField(max_length= 100)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_cita = models.ForeignKey(Tipo_Cita, on_delete=models.SET_NULL, null=True)
    actores = models.ManyToManyField(Actor, through='Actor_Cita')
    demandados = models.ManyToManyField(Demandado, through='Demandado_Cita')
    historial_EP = models.ForeignKey(Estado_Procesal_Historial, related_name='citas', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='citas_created', on_delete=models.SET_NULL, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='citas_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'citas'
    def __str__(self):
        return f"{self.historial_EP.ap.no_expediente}/{self.historial_EP.ap.year}-{self.fecha}"
    

class Actor_Cita(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'actores_has_citas'
    def __str__(self):
        return f"Cita: {self.cita}, Actor: {self.actor}"

class Demandado_Cita(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    demandado = models.ForeignKey(Demandado, on_delete=models.CASCADE)
    class Meta:
        db_table = 'demandados_has_citas'
    def __str__(self):
        return f"Cita: {self.cita}, Demandado: {self.demandado}"

class Documento_Solicitado(models.Model):
    nombre = models.CharField(max_length=100)
    detalles =models.TextField(blank=True)
    cita_demandado = models.ForeignKey(Demandado_Cita, on_delete=models.CASCADE, null=True)
    cita_actor = models.ForeignKey(Actor_Cita, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'documentos_solicitados'
    def __str__(self):
        return self.nombre