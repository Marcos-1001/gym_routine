from django.shortcuts import render
from rest_framework import viewsets, permissions
from  .serializer import UserSerializer
from .models import User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
