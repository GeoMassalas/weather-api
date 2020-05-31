
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import StationSerializer, AuthTokenSerializer, MinimalStationSerializer
from rest_framework.settings import api_settings
from core.models import Station
from django.shortcuts import get_object_or_404


class StationViewSet(viewsets.ViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Station.objects.filter(is_verified=True)
        serializer = MinimalStationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Station.objects.filter(id=request.user.id)
        user = get_object_or_404(queryset)
        serializer = StationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        data = request.data
        queryset = Station.objects.filter(id=request.user.id)
        user = get_object_or_404(queryset)
        if 'altitude' in data:
            user.altitude = data['altitude']
        if 'longitude' in data:
            user.longitude = data['longitude']
        if 'latitude' in data:
            user.latitude = data['latitude']
        if 'external_id' in data:
            user.external_id = data['external_id']
        if 'email' in data:
            user.email = data['email'].lower()
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            if 'password2' in data:
                if data['password'] == data['password2']:
                    user.password = data['password']
                else:
                    res = {'message': 'Passwords don\'t match.'}
                    return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                res = {'message': "You need password2 to confirm password."}
                return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)
        user.is_verified = False
        user.save()
        serializer = StationSerializer(user, many=False)
        res = {'message': 'Your Station is updated! While we confirm the updated data your station '
                          'will not be able to add more data.', 'result': serializer.data}
        return Response(res, status=status.HTTP_202_ACCEPTED)


class RegisterStationViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [AllowAny]


class LoginView(ObtainAuthToken):
    queryset = Station.objects.all()
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = [AllowAny]

