from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import RegisterStationViewSet, StationViewSet, LoginView

router = routers.DefaultRouter()
router.register('register', RegisterStationViewSet, basename="Register Station")
router.register('', StationViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name="token"),
    path('', include(router.urls)),
]