from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import DataStampSerializer, StationSerializer, UserSerializer
from .models import DataStamp, Station
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['POST'])
    def create_station(self, request, pk):
        usr = User.objects.get(id=pk)
        station = Station.objects.create(user=usr,
                                         external_id=request.data['external_id'],
                                         name=request.data['name'],
                                         latitude=request.data['latitude'],
                                         longitude=request.data['longitude'],
                                         altitude=request.data['altitude'])
        station.save()
        serializer = StationSerializer(station)
        res = {'message': 'Station Created!', 'result': serializer.data}
        return Response(res, status=status.HTTP_200_OK)


class DataStampViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataStamp.objects.all()
    serializer_class = DataStampSerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    @action(detail=True, methods=['POST'])
    def add_data(self, request, pk):
        data = DataStamp.objects.create(station=Station.objects.get(id=pk),
                                        temperature=request.data['temperature'],
                                        wind_speed=request.data['wind_speed'],
                                        wind_direction=request.data['wind_direction'],
                                        pressure=request.data['pressure'],
                                        humidity=request.data['humidity'],
                                        rain_1h=request.data['humidity'],)
        data.save()
        serializer = DataStampSerializer(data)
        res = {'message': 'Data added!', 'result': serializer.data}
        return Response(res, status=status.HTTP_200_OK)

