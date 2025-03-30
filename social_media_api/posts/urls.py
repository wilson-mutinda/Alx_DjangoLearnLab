from django.urls import path
from .views import PostViewSet, CommentViewSet, LikeViewSet, UserFeedView

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts'),
    path('posts/<int:post_id>/like/', LikeViewSet.as_view({'post': 'create'}), name='like-post'),
    path('posts/<int:post_id>/unlike/', LikeViewSet.as_view({'delete': 'destroy'}), name='unlike-post'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
