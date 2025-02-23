from django import forms
from .models import Book, Author, Librarian, Library

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']