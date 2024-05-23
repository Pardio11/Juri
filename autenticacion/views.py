from django.shortcuts import render
from django.http import HttpResponse
from autenticacion import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status as http_status
from autenticacion.serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({"user": user, "status":http_status.HTTP_201_CREATED})

class AccountTokenObtainPairViewSerializer(jwt_serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class AccountTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = AccountTokenObtainPairViewSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request):
    serializer = UserSerializer(request.user)
    return Response({"user": serializer.data})
