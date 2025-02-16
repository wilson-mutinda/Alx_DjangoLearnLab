from bookshelf.models import Book

book = Book.objects.filter(title="Nineteen Eighty-Four").first()
if book:
    book.delete()
    print("Book deleted successfully.")
else:
    print("Book not found.")
