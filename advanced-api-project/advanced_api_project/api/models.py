from django.db import models

"""
Models for the API.

- Author: Represents a book author.
- Book: Represents a book written by an author. Has a one-to-many relationship with Author.
"""
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
