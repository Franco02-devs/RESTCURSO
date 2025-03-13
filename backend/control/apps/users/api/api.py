from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from apps.users.models import User
from apps.users.api.serializers import CustomUserSerializer, UserListSerializer
from rest_framework.decorators import api_view

class UserViewSet(viewsets.GenericViewSet):
    serializer_class=CustomUserSerializer
    list_serializer_class=UserListSerializer
    
    def list(self, request):
        pass    
