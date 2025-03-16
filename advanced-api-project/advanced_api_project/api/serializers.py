from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
Serializers for transforming model data into JSON and handling validation.

- BookSerializer: Serializes Book instances, including validation for publication_year.
- AuthorSerializer: Serializes Author instances, including nested books.
"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
