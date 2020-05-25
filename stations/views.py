
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import StationSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings
from core.models import Station


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    authentication_classes = (TokenAuthentication,)


class RegisterStationViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [AllowAny]


class LoginView(ObtainAuthToken):
    queryset = Station.objects.all()
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = [AllowAny]

