from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    password = serializers.CharField(
        max_length=128, 
        min_length=8, 
        write_only=True,
        style={'input_type': 'password'}
    )

    email = serializers.EmailField(max_length=255, min_length=7)

    first_name = serializers.CharField(max_length=255, min_length=2)

    last_name = serializers.CharField(max_length=255, min_length=2)

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email': 'Email is already in usage'}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
    
    username = serializers.CharField(max_length=255, min_length=2)
    
    password = serializers.CharField(
        max_length=128, 
        min_length=8, 
        write_only=True,
        style={'input_type': 'password'}
    )