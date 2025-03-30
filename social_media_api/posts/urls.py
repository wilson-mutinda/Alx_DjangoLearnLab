from django.urls import path
from .views import PostViewSet, CommentViewSet, UserFeedView

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),  # ✅ Add user feed endpoint
]
