from django.db import models
from django.conf import settings
from casos.models import Caso
from tribunal.models import Juzgado_Sala
from materias.models import Materia_Juridica

class Tipo_Juicio(models.Model):
    nombre = models.CharField(max_length = 60)
    class Meta:
        db_table = 'tipos_juicios'
    def __str__(self):
        return self.nombre
    
class Tipo_Subproceso(models.Model):
    nombre = models.CharField(max_length = 60)
    class Meta:
        db_table = 'tipos_subprocesos'
    def __str__(self):
        return self.nombre

class Subproceso(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion = models.TextField(blank=True)
    class Meta:
        db_table = 'subprocesos'
    def __str__(self):
        return self.nombre
    
class Estado_Procesal(models.Model):
    nombre = models.CharField(max_length = 60)
    class Meta:
        db_table = 'estados_procesales'
    def __str__(self):
        return self.nombre
    


class Archivo_Personal(models.Model):
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    no_expediente = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField()
    tipos_juicio = models.ManyToManyField(Tipo_Juicio)
    materia_juridica = models.ForeignKey(Materia_Juridica, on_delete=models.PROTECT, null=True)
    estado_procesal_historial = models.ManyToManyField(Estado_Procesal, through='Estado_Procesal_Historial', related_name='archivos_personales_historial')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ap_created', on_delete=models.SET_NULL,null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ap_modified', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'archivos_personales'
    def __str__(self):
        return f"{self.no_expediente}/{self.year}"

class Estado_Procesal_Historial(models.Model):
    ap = models.ForeignKey(Archivo_Personal, on_delete=models.CASCADE, related_name='historial_estados_procesales')
    estado_procesal = models.ForeignKey(Estado_Procesal, on_delete=models.SET_NULL, null=True)
    juzgado_sala = models.ForeignKey(Juzgado_Sala, on_delete=models.SET_NULL, null=True, blank=True)
    subproceso = models.OneToOneField(Subproceso, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='estado_procesal_historial_created', on_delete=models.CASCADE)
    class Meta:
        db_table = 'estado_procesal_historial'
    def __str__(self):
        return f"AP: {self.ap.no_expediente}/{self.ap.year}, Estado: {self.estado_procesal.nombre}"


class Acuerdo(models.Model):
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    historial_ES = models.ForeignKey(Estado_Procesal_Historial, on_delete=models.CASCADE)
    class Meta:
        db_table = 'acuerdos'
    def __str__(self):
        return self.nombre