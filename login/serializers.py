from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model= User
        fields=('username','email', 'password')

    def create(self,validated_data):
        user=User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token['username'] =user.username
        return token
    
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields='__all__'
