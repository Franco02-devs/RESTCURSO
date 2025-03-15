from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user= User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (  'username', 'email', 'name', 'last_name')
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        
    def to_representation(self, instance):
        return {
            'username':instance['username'],
            'email':instance['email'],
            'name':instance['name']
                }
        
class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 128, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 128, min_length = 6, write_only = True)
    
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Ambas contraseñas deben ser iguales!')
        return data
        