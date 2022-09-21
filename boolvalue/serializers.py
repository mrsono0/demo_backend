from rest_framework import serializers
from .models import BoolValue

class BoolValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoolValue
        fields = ['BeautyTrue', 'HospitalTrue', 'TaxiTrue', 'HotelTrue', 'CafeTrue', 'ParkTrue', 'Hos24True']
