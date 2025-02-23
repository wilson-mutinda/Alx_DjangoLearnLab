import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 📌 Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return []

# 📌 Query 2: List all books in a library (Fixed ✅)
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # ✅ Use `get()` instead of `filter().first()`
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return []

# 📌 Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # ✅ Use `get()` for consistency
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return "Library or librarian not found"

# 🔹 Example Usage
if __name__ == "__main__":
    print("Books by 'George Orwell':", get_books_by_author("George Orwell"))
    print("Books in 'Central Library':", get_books_in_library("Central Library"))
    print("Librarian of 'Central Library':", get_librarian_for_library("Central Library"))
