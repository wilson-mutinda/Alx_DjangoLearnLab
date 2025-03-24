from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.list_create_user_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('profile/', views.user_profile_view, name='profile')
]
