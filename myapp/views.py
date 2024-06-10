from django.shortcuts import render
from .filters import SensorFilter, TemperaturafilterView, TemperaturaDataFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *

# Create your views here.
from django.shortcuts import render
from myapp import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Sensor
from rest_framework import viewsets

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Crie um novo usuário
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class SensorViewSet(viewsets.ModelViewSet):
  queryset = Sensor.objects.all()
  serializer_class = serializers.SensorSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_class = SensorFilter

@permission_classes([IsAuthenticated])
class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperaturaDataFilter

@permission_classes([IsAuthenticated]) 
class UmidadeDataViewSet(viewsets.ModelViewSet):
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer
    
@permission_classes([IsAuthenticated])
class LuminosidadeDataViewSet(viewsets.ModelViewSet):
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer

@permission_classes([IsAuthenticated])
class ContadorDataViewSet(viewsets.ModelViewSet):
    queryset = ContadorData.objects.all()
    serializer_class = serializers.ContadorDataSerializer
