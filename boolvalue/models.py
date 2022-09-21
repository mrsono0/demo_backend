from django.db import models

class BoolValue(models.Model):
    BeautyTrue = models.BooleanField(blank = True, null=True)
    HospitalTrue = models.BooleanField(blank = True, null=True)
    TaxiTrue = models.BooleanField(blank = True, null=True)
    HotelTrue = models.BooleanField(blank = True, null=True)
    CafeTrue = models.BooleanField(blank = True, null=True)
    ParkTrue = models.BooleanField(blank = True, null=True)
    Hos24True = models.BooleanField(blank = True, null=True)


