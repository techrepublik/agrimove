from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, ProductPic, Fleet, VehicleType, Vehicle, VehiclePic
from .serializers import CategorySerializer, ProductSerializer, ProductPicSerializer, FleetSerializer, VehicleTypeSerializer, VehicleSerializer, VehiclePicSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductPicViewSet(viewsets.ModelViewSet):
    queryset = ProductPic.objects.all()
    serializer_class = ProductPicSerializer

class FleetViewSet(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset =  VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehiclePicViewSet(viewsets.ModelViewSet):
    queryset = VehiclePic.objects.all()
    serializer_class = VehiclePicSerializer
