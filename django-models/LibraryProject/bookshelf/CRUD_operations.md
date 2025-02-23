# CRUD Operations for Book Model

## 1. Create a Book Instance
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)


book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id))


book.delete()
print(Book.objects.all())
