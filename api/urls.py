from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, ProductPicViewSet, FleetViewSet, VehicleTypeViewSet, VehicleViewSet, VehiclePicViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'product-pic', ProductPicViewSet, basename='product-pic')
router.register(r'fleet', FleetViewSet, basename='fleet')
router.register(r'vehicle-type', VehicleTypeViewSet, basename='vehicle-type')
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
router.register(r'vehicle-pic', VehiclePicViewSet, basename='vehicle-pic')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include(router.urls)),
] 