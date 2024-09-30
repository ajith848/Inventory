from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, InventorySerializer
from .models import *
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

# View for user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)

# View for user login using JWT
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            "access": response.data['access'],
            "refresh": response.data['refresh'],
            "message": "Login successful",
        }, status=status.HTTP_200_OK)


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class =InventorySerializer
    permission_classes = [IsAuthenticated]

class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class =InventorySerializer
    permission_classes = [IsAuthenticated]