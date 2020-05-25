from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import DataStampSerializer
from core.models import DataStamp


class DataStampViewSet(viewsets.ModelViewSet):
    queryset = DataStamp.objects.all()
    serializer_class = DataStampSerializer

