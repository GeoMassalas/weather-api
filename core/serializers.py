from rest_framework import serializers
from .models import DataStamp, Station
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class DataStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStamp
        fields = ('id', 'station', 'date', 'time', 'temperature', 'wind_speed', 'wind_direction',
                  'pressure', 'humidity', 'rain_1h')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'user', 'name', 'latitude', 'longitude', 'altitude')
