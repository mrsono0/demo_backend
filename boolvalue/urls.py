from django.urls import path, include

from .views import BeautyTrueAPI
from .views import HospitalTrueAPI
from .views import TaxiTrueAPI
from .views import HotelTrueAPI
from .views import CafeTrueAPI
from .views import ParkTrueAPI
from .views import Hos24TrueAPI

urlpatterns = [
    path('beautytrue/', BeautyTrueAPI.as_view()),
    path('hospitaltrue/', HospitalTrueAPI.as_view()),
    path('taxitrue/', TaxiTrueAPI.as_view()),
    path('hoteltrue/', HotelTrueAPI.as_view()),
    path('cafetrue/', CafeTrueAPI.as_view()),
    path('parktrue/', ParkTrueAPI.as_view()),
    path('hos24true/', Hos24TrueAPI.as_view()),
]