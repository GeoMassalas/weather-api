from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator


class StationManager(BaseUserManager):
    def create_user(self, email, username, password, external_id, latitude, longitude, altitude):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            external_id=external_id,
            latitude=latitude,
            longitude=longitude,
            altitude=altitude,
            is_verified=False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Station(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=35, unique=True)
    """ User Specific """
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    """ Station Specific """
    external_id = models.CharField(max_length=50, null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    altitude = models.PositiveSmallIntegerField(null=True)
    is_verified = models.BooleanField(default=False, null=True)

    def data(self):
        data = DataStamp.objects.filter(station=self)
        return len(data)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = StationManager()

    def __str__(self):
        return self.username


class DataStamp(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False)

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
    temperature = models.DecimalField(max_digits=3, decimal_places=1,
                                      validators=[MinValueValidator(-50), MaxValueValidator(80)])
    wind_speed = models.DecimalField(max_digits=4, decimal_places=1)
    wind_direction = models.CharField(max_length=2, choices=WIND_DIRECTIONS)
    # TODO: Not really sure how to validate atmospheric pressure. Need to do further research.
    pressure = models.PositiveSmallIntegerField()
    humidity = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(40)])
    rain_1h = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.date
