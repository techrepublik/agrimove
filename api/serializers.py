from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import CustomUser

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'mobile_no', 'password', 'last_name', 'first_name', 'middle_name', 'home_address', 'user_type', 'picture')

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'mobile_no', 'last_name', 'first_name', 'middle_name', 'home_address', 'user_type', 'picture')
