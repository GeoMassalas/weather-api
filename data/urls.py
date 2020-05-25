from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import DataStampViewSet

router = routers.DefaultRouter()
router.register('', DataStampViewSet, basename="Data")

urlpatterns = [
    path('', include(router.urls))
]
