# Retrieve Book Instance

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")  # Retrieves the book by title
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
