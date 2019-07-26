from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import userAddress

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'last_name', 'user_phone', "user_signature", "user_address", "user_img")

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(UserSerializer):
    id = serializers.IntegerField(required=True)

class addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAddress
        fields = ("__all__")

class addressDeleteSerializer(addressSerializer):
    class Meta:
        model = userAddress
        fields = ("id", )