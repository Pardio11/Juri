from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes),
    path('abogado/<int:licenciado_id>/', views.licenciado_detalles),
    path('abogados/', views.lista_abogados),
    path('cliente/<int:cliente_id>/', views.cliente_detalles),
    path('cliente_datos/<int:cliente_id>/', views.casos_citas_documentos_cliente),
]