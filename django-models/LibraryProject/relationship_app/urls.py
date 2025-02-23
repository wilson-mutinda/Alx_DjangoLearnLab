from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import relationship_app.views as views  # Import views explicitly

import relationship_app.views as views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view', views.librarian_view, name='librarian_view'),
    path('member-view', views.member_view, name='member_view'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Explicitly reference views.register
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
