from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from datetime import datetime
from .serializers import CasoSerializer
from .models import Caso
from archivos_personales.serializers import APSerializer, EPHSerializer
from involucrados.serializers import DemandadoSerializer, ActorSerializer
from django.utils import timezone

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_caso(request):
    form_data = request.data
    form_caso_data = form_data.get('formCasoData')
    form_ap_data = form_data.get('formAPData')
    form_eph_data = form_data.get('formEPHData')
    form_actores_data = form_data.get('formActoresData')
    form_demandados_data = form_data.get('formDemandadosData')

    if form_caso_data:
        form_caso_data['created_by'] = request.user.id
        form_caso_data['modified_by'] = request.user.id
        serializer_caso = CasoSerializer(data=form_caso_data)
        serializer_caso.is_valid(raise_exception=True)

        with transaction.atomic():
            caso = serializer_caso.save()
            caso_id = caso.id
            current_datetime = timezone.localtime(timezone.now())
            current_year = current_datetime.year
            archivo_personal_data = {
                'caso': caso_id,
                'year': current_year,
                'created_by': request.user.id,
                'modified_by': request.user.id,
                **form_ap_data  
            }
            archivo_personal_serializer = APSerializer(data=archivo_personal_data)
            archivo_personal_serializer.is_valid(raise_exception=True)
            archivo_personal = archivo_personal_serializer.save()
            archivo_personal_id = archivo_personal.id
            estado_procesal_data = {
                'ap': archivo_personal.id,
                'estado_procesal': form_eph_data['estado_procesal'],
                'created_by': request.user.id,
            }
            estado_procesal_hist_serializer = EPHSerializer(data=estado_procesal_data)
            estado_procesal_hist_serializer.is_valid(raise_exception=True)
            estado_procesal_hist_serializer.save()
            # Create actors
            for actor_data in form_actores_data:
                actor_data['archivo_personal'] = archivo_personal_id
                actor_serializer = ActorSerializer(data=actor_data)
                actor_serializer.is_valid(raise_exception=True)
                actor_serializer.save()

            # Create defendants
            for demandado_data in form_demandados_data:
                demandado_data['archivo_personal'] = archivo_personal_id
                demandado_serializer = DemandadoSerializer(data=demandado_data)
                demandado_serializer.is_valid(raise_exception=True)
                demandado_serializer.save()

        return Response(serializer_caso.data, status=status.HTTP_201_CREATED)

    else:
        raise ValidationError("formCasoData, formAPData, formEPHData, formActoresData & formDemandadosData are required.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_casos(request):
    casos = Caso.objects.all()
    serializer = CasoSerializer(casos, many=True)
    return JsonResponse({"casos": serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def casos_cliente(request, cliente_id):
    try:
        casos = Caso.objects.filter(cliente_id=cliente_id)
        serializer = CasoSerializer(casos, many=True)
        return JsonResponse({"casos": serializer.data})
    except Caso.DoesNotExist:
        return JsonResponse({"message": "No se encontraron casos para el cliente dado."}, status=404)