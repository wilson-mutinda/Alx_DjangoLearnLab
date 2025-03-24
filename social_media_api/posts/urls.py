from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.PostViewSet.as_view(), name='posts'),
    path('comments/', views.CommentViewSet.as_view(), name='comments'),
]