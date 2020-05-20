from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    external_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=35, null=False)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)
    altitude = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class DataStamp(models.Model):
    # TODO: I would like to keep the measurement even if the station gets deleted
    #       so i need to do further research on how to keep it(on_delete=???).
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True)

    WIND_DIRECTIONS = [
        ('W', 'West'),
        ('E', 'East'),
        ('N', 'North'),
        ('S', 'South'),
        ('SE', 'SouthEast'),
        ('SW', 'SouthWest'),
        ('NE', 'NorthEast'),
        ('NW', 'NorthWest')
    ]
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    wind_speed = models.DecimalField(max_digits=3, decimal_places=1)
    wind_direction = models.CharField(max_length=2, choices=WIND_DIRECTIONS)
    pressure = models.PositiveSmallIntegerField()
    humidity = models.PositiveSmallIntegerField()
    rain_1h = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.date
