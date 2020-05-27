
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
from django.shortcuts import get_object_or_404


class StationViewSet(viewsets.ViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = Station.objects.filter(id=request.user.id)
        user = get_object_or_404(queryset)
        serializer = StationSerializer(user)
        return Response(serializer.data)


class RegisterStationViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [AllowAny]


class LoginView(ObtainAuthToken):
    queryset = Station.objects.all()
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = [AllowAny]

