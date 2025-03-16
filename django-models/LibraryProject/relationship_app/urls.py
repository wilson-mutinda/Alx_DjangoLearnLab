from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books  # ✅ Explicitly import list_books
import relationship_app.views as views  # Keep this for other views
from relationship_app.views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book-related URLs
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', list_books, name='list_books'),  # ✅ Use directly imported function

    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
