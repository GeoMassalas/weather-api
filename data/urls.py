from django.urls import path
from .views import DataStampView


urlpatterns = [
    path('', DataStampView.as_view(), name="Data")
]
