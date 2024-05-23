from django.contrib import admin
from .models import Tipo_Juicio, Estado_Procesal,Archivo_Personal, Estado_Procesal_Historial

admin.site.register(Archivo_Personal)
admin.site.register(Estado_Procesal_Historial)
admin.site.register(Tipo_Juicio)
admin.site.register(Estado_Procesal)