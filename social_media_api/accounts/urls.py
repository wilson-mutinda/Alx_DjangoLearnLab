from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('profile/', views.user_profile_view, name='profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    # path('feed/', views.user_feed, name='user_feed'),
]
