from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.db import transaction
from .models import Cliente, Licenciado
from casos.models import Caso
from archivos_personales.models import Archivo_Personal, Estado_Procesal_Historial
from citas.models import Cita
from documentos.models import Documento_Cliente
from .serializers import ClienteSerializer, LicenciadoSerializer
from citas.serializers import CitaSerializer
from casos.serializers import CasoSerializer
from documentos.serializers import DocumentoClienteSerializer
from rest_framework.permissions import IsAuthenticated
from autenticacion.serializers import RegisterSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return JsonResponse({"clientes": serializer.data})
    
    if request.method == 'POST':
        form_user_data  = request.data.get('formUserData')
        form_client_data = request.data.get('formClientData')
        with transaction.atomic():
            if form_client_data is not None:
                if form_user_data is not None and form_client_data is not None :
                    serializer = RegisterSerializer(data=form_user_data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    user_id = user.id
                    form_client_data['usuario'] = user_id
                
                serializerCliente = ClienteSerializer(data=form_client_data)
                serializerCliente.is_valid(raise_exception=True)
                serializerCliente.save()
                return Response(serializerCliente.data, status=status.HTTP_201_CREATED)
            else:
                raise ValidationError("formClientData is required.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cliente_detalles(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        serializer = ClienteSerializer(cliente)
        return JsonResponse({"cliente": serializer.data})
    except Cliente.DoesNotExist:
        return JsonResponse({"message": "No se encontró ningún cliente con el ID proporcionado."}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def casos_citas_documentos_cliente(request, cliente_id):
    try:
        documentos = Documento_Cliente.objects.filter(cliente=cliente_id)
        casos = Caso.objects.filter(cliente=cliente_id)
        citas = Cita.objects.filter( historial_EP__ap__caso__cliente_id=cliente_id)
        documentos_serializer = DocumentoClienteSerializer(documentos, many=True)
        casos_serializer = CasoSerializer(casos, many=True)
        citas_serializer = CitaSerializer(citas, many=True)

        response_data = {
            "documentos": documentos_serializer.data,
            "casos": casos_serializer.data,
            "citas": citas_serializer.data
        }

        return Response(response_data)

    except Cliente.DoesNotExist:
        return Response({"error": f"Cliente with id {cliente_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_abogados(request):
    if request.method == 'GET':
        abogados = Licenciado.objects.all()
        serializer = LicenciadoSerializer(abogados, many=True)
        return JsonResponse({"abogados": serializer.data})
    
    if request.method == 'POST':
        form_user_data  = request.data.get('formUserData')
        form_abogado_data = request.data.get('formAbogadoData')
        
        # Check if form_user_data is not None
        if form_user_data is not None and form_abogado_data is not None:
            serializer = RegisterSerializer(data=form_user_data)
            serializerLicenciado = LicenciadoSerializer(data=form_abogado_data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                user = serializer.save()
                user_id = user.id
                form_abogado_data['usuario'] = user_id
                serializerLicenciado.is_valid(raise_exception=True)
                serializerLicenciado.save()
                return Response(serializerLicenciado.data, status=status.HTTP_201_CREATED)
        else:
            raise ValidationError("Both formUserData and formAbogadoData are required.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def licenciado_detalles(request, licenciado_id):
    try:
        licenciado = Licenciado.objects.get(id=licenciado_id)
        serializer = LicenciadoSerializer(licenciado)
        return JsonResponse({"licenciado": serializer.data})
    except Licenciado.DoesNotExist:
        return JsonResponse({"message": "No se encontró ningún licenciado con el ID proporcionado."}, status=404)
        
""" @api_view(['GET'])
@permission_classes([IsAuthenticated])
def casos_licenciado(request, licenciado_id):
    try:
        casos = Caso.objects.filter(id=licenciado_id)
        serializer = CasoSerializer(casos, many=True)
        return JsonResponse({"casos": serializer.data})
    except Caso.DoesNotExist:
        return JsonResponse({"message": "No se encontraron casos para el licenciado dado."}, status=404)
     """
  
        