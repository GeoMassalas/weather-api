from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class StationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'password2', 'email', 'external_id', 'latitude', 'longitude',
                  'altitude', 'data')
        extra_kwargs = {'password': {'style': {'input_type': 'password'}, 'write_only': True,
                                     'required': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match.")
        if data['longitude'] is not None:
            if abs(data['longitude']) > 180:
                raise serializers.ValidationError("Longitude should be from -180 to 180 degrees")
        if data['latitude'] is not None:
            if abs(data['latitude']) > 90:
                raise serializers.ValidationError("Latitude should be from -90 to 90 degrees")

        del data['password2']
        return data


class MinimalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'external_id', 'latitude', 'longitude',
                  'altitude', 'data')


class DisplayStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'external_id', 'latitude', 'longitude',
                  'altitude', 'data')
        extra_kwargs = {'password': {'write_only': True, 'required': True, 'min_length': 8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
