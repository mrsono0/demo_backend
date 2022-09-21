"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from park.views import ParkAPI
from emhospital.views import EmHospitalAPI
# from Bessel.views import filteringBessel
# from Point.views import filteringPoint
urlpatterns = [
    path('admin/', admin.site.urls),
    path('infra/', include('infra.urls')),
    path('park/', ParkAPI.as_view()),
    path('boolvalue/', include('boolvalue.urls')),
    path('emhospital/', EmHospitalAPI.as_view()),
    # path('bessel/', filteringBessel.as_view()),
    # path('point/', filteringPoint.as_view()),
]
