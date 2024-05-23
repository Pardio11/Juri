from django.urls import path
from . import views

urlpatterns = [
    path('casos/', views.lista_casos),
    path('crearcaso/', views.crear_caso),
    path('casos/<int:cliente_id>', views.casos_cliente),
]
