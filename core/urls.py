from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import DataStampViewSet, StationViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('data', DataStampViewSet)
router.register('stations', StationViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
