from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializers import InfraSerializer
from .models import Infra

class InfraBeautyAPI(APIView):
    def get(self, request):
        InfraBeauty = Infra.objects.filter(InfraWork='애견미용')
        serializer = InfraSerializer(InfraBeauty, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InfraHospitalAPI(APIView):
    def get(self, request):
        InfraHospital = Infra.objects.filter(InfraWork='동물병원')
        serializer = InfraSerializer(InfraHospital, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InfraTaxiAPI(APIView):
    def get(self, request):
        InfraTaxi = Infra.objects.filter(InfraWork='펫택시')
        serializer = InfraSerializer(InfraTaxi, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InfraHotelAPI(APIView):
    def get(self, request):
        InfraBeauty = Infra.objects.filter(InfraWork='펫호텔')
        serializer = InfraSerializer(InfraBeauty, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InfraCafeAPI(APIView):
    def get(self, request):
        InfraCafe = Infra.objects.filter(InfraWork='펫카페')
        serializer = InfraSerializer(InfraCafe, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
