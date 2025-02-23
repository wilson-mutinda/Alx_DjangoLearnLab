from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Author, Book, Librarian, Library

def list_all_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"