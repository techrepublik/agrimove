from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import CustomUser, Category, Product, ProductPic, Fleet, VehicleType, Vehicle, VehiclePic      
from rest_framework import serializers

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'mobile_no', 'password', 'last_name', 'first_name', 'middle_name', 'home_address', 'user_type', 'picture')

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'mobile_no', 'last_name', 'first_name', 'middle_name', 'home_address', 'user_type', 'picture')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'product_name', 'product_description')

class ProductPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPic
        fields = ('id', 'product', 'product_pic_pic_image', 'product_pic_name')

class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet       
        fields = ('id', 'fleet_owner', 'fleet_name', 'fleet_description', 'fleet_picture')

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('id', 'vehicle_type_name', 'vehicle_type_description', 'vehicle_type_start_price', 'vehicle_class_kg')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'vehicle_owner', 'vehicle_type', 'vehicle_class', 'fleet', 'plate_no', 'vehicle_type', 'vehicle_model', 'vehicle_year', 'vehicle_color', 'vehicle_capacity', 'vehicle_description', 'vehicle_or_cr_pic')

class VehiclePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePic
        fields = ('id', 'vehicle', 'image', 'pic_name')