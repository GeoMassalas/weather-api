from rest_framework import serializers
from core.models import DataStamp


class DataStampSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataStamp
        fields = ('id', 'station', 'date', 'time', 'temperature', 'wind_speed', 'wind_direction',
                  'pressure', 'humidity', 'rain_1h')

    def validate(self, data):
        # TODO: No validation for atmospheric pressure yet. Need to do more research on units.
        if data['temperature'] is not None:
            if (data['temperature'] > 80) | (data['temperature'] < -80):
                raise serializers.ValidationError("Temperature should be between -80 and 80 degrees C.")
        if data['humidity'] is not None:
            if data['humidity'] > 100:
                raise serializers.ValidationError("Humidity should be between 0 and 100%.")
        if data['wind_speed'] is not None:
            if data['wind_speed'] > 800 | data['wind_speed'] < 0:
                raise serializers.ValidationError("Wind speed should be between 0 and 800 Km/s.")
        if data['rain_1h'] is not None:
            if data['rain_1h'] > 500 | data['wind_speed'] < 0:
                raise serializers.ValidationError("Rain per hour should be between 0 and 500 mms.")

        return data
