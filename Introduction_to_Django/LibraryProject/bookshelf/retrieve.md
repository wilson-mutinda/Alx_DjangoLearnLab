from bookshelf.models import Book

book = Book.objects.filter(title="1984").first()  # Retrieves the first matching book
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
