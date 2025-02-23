from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    search_fields = ('title', 'author')  # Allow searching by title and author
    list_filter = ('publication_year',)  # Add filter for publication year
