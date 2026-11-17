
from django.db import models


class Zonas(models.Model):
    numero_plazas = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class PlazasLibres(models.Model):
    zona = models.ForeignKey(
        Zonas,
        on_delete=models.CASCADE,
        related_name='registros_plazas'
    )

    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    plazas_libres = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.zona} - {self.hora_inicio} / {self.hora_fin}"
