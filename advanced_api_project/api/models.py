from django.db import models

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book, linked to an author."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

