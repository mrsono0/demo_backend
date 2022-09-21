from rest_framework import serializers
from .models import Infra

class InfraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infra
        fields = ['InfraGoo', 'InfraDong', 'InfraWork', 'InfraName', 'Latitude', 'Longitude']
