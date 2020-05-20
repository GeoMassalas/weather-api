from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import DataStamp, Station


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True, 'min_length': 6}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class DataStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStamp
        fields = ('id', 'station', 'date', 'time', 'temperature', 'wind_speed', 'wind_direction',
                  'pressure', 'humidity', 'rain_1h')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'external_id', 'user', 'name', 'latitude', 'longitude', 'altitude')
