from dataclasses import field
from .models import User
from rest_framework import serializers

 
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

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'location_gu', 'location_city']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'password', 'nickname']