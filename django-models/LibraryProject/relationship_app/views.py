from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Library

from .models import Author, Book, Librarian

def list_all_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"