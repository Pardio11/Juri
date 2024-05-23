from django.db import models
from django.conf import settings

class Persona(models.Model):
    nombres = models.CharField(max_length= 100)
    apellido_paterno = models.CharField(max_length= 40)
    apellido_materno = models.CharField(max_length= 40, blank=True)
    curp = models.CharField(max_length= 18, blank=True)
    rfc = models.CharField(max_length= 13, blank=True)
    genero = models.CharField(max_length= 1, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.EmailField(max_length= 120)
    telefono = models.CharField(max_length= 20, blank=True)
    lugar_nacimiento = models.CharField(max_length= 150, blank=True)
    domicilio_calle = models.CharField(max_length= 100, blank=True)
    domicilio_num_ext = models.CharField(max_length= 14, blank=True)
    domicilio_num_int = models.CharField(max_length= 14, blank=True)
    domicilio_colonia = models.CharField(max_length= 80, blank=True)
    domicilio_municipio = models.CharField(max_length= 80, blank=True)
    domicilio_estado = models.CharField(max_length= 80, blank=True)
    domicilio_pais = models.CharField(max_length= 80, blank=True)
    domicilio_codigo_postal = models.CharField(max_length= 5, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    class Meta:
        abstract = True  # Define el modelo como abstracto para que no se cree una tabla en la base de datos

class Cliente(Persona):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        db_table = 'clientes'

class Licenciado(Persona):
    cedula_profesional = models.CharField(max_length=20, blank=True)
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        db_table = 'licenciados'

