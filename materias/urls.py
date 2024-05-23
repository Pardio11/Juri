from django.urls import path
from . import views

urlpatterns = [
    path('materias/', views.lista_materias),
    path('crearmateria/', views.crear_materia),
]