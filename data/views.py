from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .serializers import DataStampSerializer
from core.models import DataStamp


class DataStampFilter(filters.FilterSet):
    min_temp = filters.NumberFilter(field_name="temperature", lookup_expr='gte')
    max_temp = filters.NumberFilter(field_name="temperature", lookup_expr='lte')
    min_date = filters.DateFilter(field_name="date", lookup_expr='gte')
    max_date = filters.DateFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = DataStamp
        fields = ['station', 'min_temp', 'max_temp', 'min_date', 'max_date', 'station__external_id']


class DataStampView(ListCreateAPIView):
    queryset = DataStamp.objects.all()
    serializer_class = DataStampSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    # Filtering
    filterset_class = DataStampFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter()
        serializer = DataStampSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        station = request.user
        if station.is_verified:

            temperature = request.data['temperature']
            wind_speed = request.data['wind_speed']
            wind_direction = request.data['wind_direction']
            pressure = request.data['pressure']
            humidity = request.data['humidity']
            rain_1h = request.data['rain_1h']
            data_stamp = DataStamp.objects.create(station=station,
                                                  temperature=temperature,
                                                  wind_speed=wind_speed,
                                                  wind_direction=wind_direction,
                                                  pressure=pressure,
                                                  humidity=humidity,
                                                  rain_1h=rain_1h)
            data_stamp.save()
            serializer = DataStampSerializer(data_stamp, many=False)
            res = {'message': 'New Data Added', 'result': serializer.data}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            res = {'message': 'Station is not verified. Please contact a system administrator.'}
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)