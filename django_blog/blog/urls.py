from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('list/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Change 'create/' to 'new/'
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Change 'edit/' to 'update/'
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]