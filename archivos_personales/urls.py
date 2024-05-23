from django.urls import path
from . import views

urlpatterns = [
    path('tiposjuicio/', views.lista_tipos_juicio),
    path('estadosprocesales/', views.lista_estados_procesales),
    path('creartipojucio/', views.crear_tipo_juicio),
    path('crearestadoprocesal/', views.crear_estado_procesal),
]