from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import Car
from api_app.serializers import CarSerializer


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


