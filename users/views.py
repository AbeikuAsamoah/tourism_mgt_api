from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserDetailSerializer
from rest_framework.authtoken.views import ObtainAuthTokenom django.shortcuts import render

# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]  # anyone can register

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # create token for the new user
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response

# Login endpoint (returns token)
class UserLoginView(ObtainAuthToken):
    """Returns authentication token for existing user"""
    pass
