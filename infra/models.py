from django.db import models

class Infra(models.Model):
    InfraGoo = models.CharField(max_length=20)
    InfraDong = models.CharField(max_length=20)
    InfraWork = models.CharField(max_length=20)
    InfraName = models.CharField(max_length=50)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
