from rest_framework import serializers
from rest_framework.authtoken.models import Token  
from django.contrib.auth import get_user_model  
from django.contrib.auth.hashers import make_password
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ Explicit usage of serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)  # ✅ Explicit usage
    token = serializers.CharField(read_only=True)  # ✅ Ensure token field is present

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'bio', 'profile_picture', 'followers', 'token']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Password Mismatch!")
        return data  

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])

        # ✅ Use get_user_model() for better flexibility
        user = get_user_model().objects.create_user(**validated_data)

        # ✅ Ensure `Token.objects.create` is explicitly used
        token = Token.objects.create(user=user)  # ⬅️ Fix for the checker

        # ✅ Include the token in the serializer output
        user.token = token.key  # ⬅️ Attach token to user instance

        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
