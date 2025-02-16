from bookshelf.models import Book

book = Book.objects.filter(title="1984").first()  # Use `.first()` to get one instance
if book:
    book.title = "Nineteen Eighty-Four"
    book.save()
    print(f"Updated Book Title: {book.title}")
