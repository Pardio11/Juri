from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MateriaSerializer
from .models import Materia_Juridica

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_materias(request):
    materias = Materia_Juridica.objects.all()
    serializer = MateriaSerializer(materias, many=True)
    return JsonResponse({"materias": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_materia(request):
    if request.method == 'POST':
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)