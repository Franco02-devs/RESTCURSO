from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from apps.users.models import User
from apps.users.api.serializers import CustomUserSerializer, UserListSerializer, UpdateUserSerializer, PasswordSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class=CustomUserSerializer
    list_serializer_class=UserListSerializer
    queryset=None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
        
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active = True).values('username','email','name')
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
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk= pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk=pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente',
            }, status=status.HTTP_200_OK
                            )
        return Response({
            'message': 'Error',
            'errors': user_serializer.errors    
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods= ['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk = pk)
        password_serializer = PasswordSerializer( data = request.data)
        
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message':'Contraseña actualizada'
            },status=status.HTTP_200_OK)
        return Response({
                'errors':'Error en el registro'
            },status=status.HTTP_400_BAD_REQUEST)
                          
        
    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id = pk).update(is_active = False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message':'No existe dicho usuario',
        },status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
            
