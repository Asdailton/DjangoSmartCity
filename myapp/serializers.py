from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username","email", "password")

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'tipo', 'mac_address', 'latitude', 'longitude', 'localizacao', 'responsavel', 'unidade_medida', 'status_operacional', 'observacao']

class TemperaturaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'


class UmidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData
        fields = '__all__'

class LuminosidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData
        fields = '__all__'

class ContadorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContadorData
        fields = '__all__'

        

