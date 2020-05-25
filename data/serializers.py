from rest_framework import serializers
from core.models import DataStamp


class DataStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStamp
        fields = ('id', 'station', 'date', 'time', 'temperature', 'wind_speed', 'wind_direction',
                  'pressure', 'humidity', 'rain_1h')
