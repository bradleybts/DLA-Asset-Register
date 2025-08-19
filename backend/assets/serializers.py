from rest_framework import serializers
from .models import Asset, CustomUser, UserClass

class UserClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClass
        fields = ['id', 'name']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['asset_name', 'asset_type', 'serial_number', 'purchase_date', 'assigned_to', 'notes']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'access_level', 'first_name', 'last_name']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            access_level=validated_data.get('access_level'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
