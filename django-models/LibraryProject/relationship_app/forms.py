from django import forms
from .models import Book, Author, Librarian, Library

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = []