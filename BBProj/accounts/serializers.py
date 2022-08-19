from dataclasses import field
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['username', 'name', 'password']
 
class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username'
        ]

class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname']