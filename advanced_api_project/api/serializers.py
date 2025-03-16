from rest_framework import serializers
from .models import Book, Author

# Serializer for the book model
class BookSerializer(serializers.ModelSerializer):
    publication_year = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, year):
        if year > 2025:
            raise serializers.ValidationError("Publication year is not in the future!")
        return year

# serializer for the author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']