from django.db import models

# Create your models here.

class Incident(models.Model):
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    class Severity(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
    severity = models.CharField(
        max_length=6,
        choices=Severity.choices
    )

    class Status(models.TextChoices):
        ACTIVE = 'RECEIVED', 'Received'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELED = 'CANCELED', 'Canceled'
    status = models.CharField(
        max_length=11,
        choices=Status.choices
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)