from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_view(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user)
        return response.Response({
            'message': 'User created successfully!',
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return response.Response({'error': 'Both username and password are required!'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
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
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return response.Response({'error': 'Unauthorized!'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_follow:
        return response.Response({'error': 'You cannot follow yourself!'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    return response.Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if request.user == user_to_unfollow:
        return response.Response({'error': 'You cannot unfollow yourself!'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.remove(user_to_unfollow)
    return response.Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_feed(request):
#     followed_users = request.user.following.all()
#     posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
#     serializer = PostSerializer(posts, many=True)
#     return response.Response(serializer.data, status=status.HTTP_200_OK)

