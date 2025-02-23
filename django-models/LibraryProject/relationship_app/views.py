from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Author, Book, Librarian, Library

def list_all_books(request):
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"<pre>{book_list}</pre>")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"