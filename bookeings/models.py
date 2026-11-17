from django.db import models

# Create your models here.
class Booking(models.Model):
    ReserveHour = models.DateTimeField()
    active = models.BooleanField(default=True)

    # Relación usuario
    # Relación Vehículo