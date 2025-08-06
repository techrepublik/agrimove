from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random
import os

def random_filename(instance, filename):
    """Generate a random 10-digit filename while preserving the file extension"""
    ext = filename.split('.')[-1]
    random_name = str(random.randint(1000000000, 9999999999))
    return f'{random_name}.{ext}'

def user_pic_upload_path(instance, filename):
    """Upload path with random filename for user pictures"""
    return f'user_pics/{random_filename(instance, filename)}'

def product_pic_upload_path(instance, filename):
    """Upload path with random filename for product pictures"""
    return f'product_pics/{random_filename(instance, filename)}'

def catagory_pic_upload_path(instance, filename):
    """Upload path with random filename for catagory pictures"""
    return f'catagory_pics/{random_filename(instance, filename)}'

def fleet_pic_upload_path(instance, filename):
    """Upload path with random filename for fleet pictures"""
    return f'fleet_pics/{random_filename(instance, filename)}'

def vehicle_pic_upload_path(instance, filename):
    """Upload path with random filename for vehicle pictures"""
    return f'vehicle_pics/{random_filename(instance, filename)}'

class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_no, password=None, **extra_fields):
        if not mobile_no:
            raise ValueError("The Mobile Number must be set")
        user = self.model(mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(mobile_no, password, **extra_fields)

SEX_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('customer', 'Customer'),
    ('owner', 'Owner'),
    ('guest', 'Guest'),
)

VEHICLE_CLASS_CHOICES = (
    ('mini', 'Mini'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('extra_large', 'Extra Large'),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    mobile_no = models.CharField(max_length=15, unique=True)
    home_address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True) 
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='guest')
    picture = models.ImageField(upload_to=user_pic_upload_path, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.mobile_no
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=catagory_pic_upload_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class ProductPic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_pic_pic_image = models.ImageField(upload_to=product_pic_upload_path, blank=True, null=True)
    product_pic_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    
class Fleet(models.Model):
    fleet_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fleet_name = models.CharField(max_length=255)
    fleet_description = models.TextField(blank=True, null=True)
    fleet_picture = models.ImageField(upload_to=fleet_pic_upload_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fleet_name
    
class VehicleType(models.Model):
    """
    Vehicle Type is the type of the vehicle. Contains fruits, vegetables, fish, meat, and other.
    """
    vehicle_type_name = models.CharField(max_length=255)
    vehicle_class_kg = models.IntegerField(default=0)
    vehicle_type_description = models.TextField(blank=True, null=True)
    vehicle_type_start_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_class_name
    
class Vehicle(models.Model):
    vehicle_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_type = models.ManyToManyField(VehicleType, blank=True, null=True)
    vehicle_class = models.CharField(choices=VEHICLE_CLASS_CHOICES, max_length=255)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    plate_no = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    vehicle_year = models.CharField(max_length=255)
    vehicle_color = models.CharField(max_length=255)
    vehicle_capacity = models.IntegerField(default=0)
    vehicle_description = models.TextField(blank=True, null=True)
    vehicle_or_cr_pic = models.ImageField(upload_to=vehicle_pic_upload_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class VehiclePic(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=vehicle_pic_upload_path, blank=True, null=True)
    pic_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle.name

