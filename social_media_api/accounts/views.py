from django.shortcuts import render

from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import response, status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

# User creation
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])

def list_create_user_view(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many = True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    return response.Response({'error': 'Unauthorized!'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])

def user_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return response.Response({'error': 'Both username and password are required!'}, status= status.HTTP_400_BAD_REQUEST)
    
    user  = authenticate(username = username, password = password)

    if not user:
        return response.Response({'error': 'Invalid Credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh_token = RefreshToken.for_user(user)
    access_token = str(refresh_token.access_token)

    return response.Response({
        "user_email": user.email,
        "access_token": access_token,
        "refresh_token": str(refresh_token),
    }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    user = request.user

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CustomUserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return response.Response({'error': 'Unauthorized!'}, status=status.HTTP_401_UNAUTHORIZED)

