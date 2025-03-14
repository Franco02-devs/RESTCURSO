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
    queryset=None
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active = True).values('username','email','name')
        return self.queryset          
    
    def list(self, request):
        users= self.get_queryset()
        user_serializer = self.list_serializer_class(users, many = True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message' : 'Usuario registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(
            {
                'message': 'Errores en el registro',
                'errors': user_serializer.errors
            },status=status.HTTP_400_BAD_REQUEST
        )
            
