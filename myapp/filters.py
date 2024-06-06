import django_filters
from myapp.models import Sensor, TemperaturaData, UmidadeData, LuminosidadeData, ContadorData
from rest_framework import permissions
from myapp.serializers import SensorSerializer, TemperaturaDataSerializer, UmidadeDataSerializer, LuminosidadeDataSerializer, ContadorDataSerializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response

class SensorFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tipo = request.data.get('tipo', None)
        localizacao = request.data.get('localizacao', None)
        responsavel = request.data.get('responsavel', None)
        status_operacional = request.data.get('status_operacional', None)
        filters = Q()
        if tipo:
            filters &= Q(tipo__icontains=tipo)
        if localizacao:
            filters &= Q(localizacao__icontains=localizacao)
        if responsavel:
            filters &= Q(responsavel__icontains=responsavel)
        if status_operacional is not None:
            filters &= Q(status_operacional=status_operacional)
        queryset = Sensor.objects.filter(filters)
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

class SensorFilter(django_filters.FilterSet):
    responsavel = django_filters.CharFilter(field_name='responsavel', lookup_expr='icontains')
    status_operacional = django_filters.CharFilter(field_name='status_operacional', lookup_expr='exact')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='icontains')
    localizacao = django_filters.CharFilter(field_name='localizacao', lookup_expr='icontains')
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact' )

    class Meta:
        model = Sensor
        fields = ['id', 'responsavel', 'status_operacional', 'tipo', 'localizacao']

class TemperaturafilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)

        queryset = TemperaturaData.objects.filter(filters)
        serializer = TemperaturaDataSerializer(queryset, many=True)
        response_data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        return Response(response_data)
        return Response(response_data)
class TemperaturaDataFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    timestamp_lte = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')
    sensor = django_filters.NumberFilter(field_name='sensor')
    valor_gte = django_filters.NumberFilter(field_name='valor', lookup_expr='gte')
    valor_lte = django_filters.NumberFilter(field_name='valor', lookup_expr='lte')

    class Meta:
        model = TemperaturaData
        fields = ['timestamp_gte', 'timestamp_lte', 'sensor', 'valor_gte', 'valor_lte']

class UmidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
        queryset = UmidadeData.objects.filter(filters)
        serializer = UmidadeDataSerializer(queryset, many=True)
        response_data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        
        return Response(response_data)


class LuminosidadeFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
        queryset = LuminosidadeData.objects.filter(filters)
        serializer = LuminosidadeDataSerializer(queryset, many=True)
        response_data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        
        return Response(response_data)


class ContadorFilterView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        sensor_id = request.data.get('sensor_id', None)
        valor_gte = request.data.get('valor_gte', None)
        valor_lt = request.data.get('valor_lt', None)
        timestamp_gte = request.data.get('timestamp_gte', None)
        timestamp_lt = request.data.get('timestamp_lt', None)

        filters = Q()
        if sensor_id:
            filters &= Q(sensor_id=sensor_id)
        if valor_gte:
            filters &= Q(valor__gte=valor_gte)
        if valor_lt:
            filters &= Q(valor__lt=valor_lt)
        if timestamp_gte:
            filters &= Q(timestamp__gte=timestamp_gte)
        if timestamp_lt:
            filters &= Q(timestamp__lt=timestamp_lt)
        queryset = ContadorData.objects.filter(filters)
        serializer = ContadorDataSerializer(queryset, many=True)
        response_data = {
            'count': queryset.count(),
            'results': serializer.data
        }
        return Response(response_data)
