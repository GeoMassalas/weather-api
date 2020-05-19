from rest_framework import viewsets
from .serializers import DataStampSerializer, StationSerializer, UserSerializer
from .models import DataStamp, Station
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DataStampViewSet(viewsets.ModelViewSet):
    queryset = DataStamp.objects.all()
    serializer_class = DataStampSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
