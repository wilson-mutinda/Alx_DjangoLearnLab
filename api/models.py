from django.db import models

# Model to represent an author
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model to represent a book
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.title} by ({self.author.name})'
