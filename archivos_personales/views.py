from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TipoJuicioSerializer,EstadoProcesalSerializer
from .models import Tipo_Juicio,Estado_Procesal

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_tipos_juicio(request):
    tipos_juicio = Tipo_Juicio.objects.all()
    serializer = TipoJuicioSerializer(tipos_juicio, many=True)
    return JsonResponse({"tipos_juicio": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_tipo_juicio(request):
    if request.method == 'POST':
        serializer = TipoJuicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_estados_procesales(request):
    estados_procesales = Estado_Procesal.objects.all()
    serializer = EstadoProcesalSerializer(estados_procesales, many=True)
    return JsonResponse({"estados_procesales": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_estado_procesal(request):
    if request.method == 'POST':
        serializer = EstadoProcesalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
