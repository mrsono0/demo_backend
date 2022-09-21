from django.urls import path, include
from .views import InfraHospitalAPI
from .views import InfraBeautyAPI
# from .views import InfraTaxiAPI
from .views import InfraCafeAPI
from .views import InfraHotelAPI

urlpatterns = [
    path('hospital/', InfraHospitalAPI.as_view()),
    path('beauty/', InfraBeautyAPI.as_view()),
    # path('taxi/', InfraTaxiAPI.as_view()),
    path('cafe/', InfraCafeAPI.as_view()),
    path('hotel/', InfraHotelAPI.as_view()),
]
