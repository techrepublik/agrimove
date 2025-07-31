from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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

class CustomUser(AbstractBaseUser, PermissionsMixin):
    mobile_no = models.CharField(max_length=15, unique=True)
    home_address = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True) 
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='male')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='guest')
    picture = models.ImageField(upload_to='user_pics/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.mobile_no
