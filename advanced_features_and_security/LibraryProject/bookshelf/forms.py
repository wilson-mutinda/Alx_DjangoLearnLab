from django import forms
from .models import Book  # Import the Book model if it's used in the form

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Assuming 'Book' is the model you want to use
        fields = ['title', 'author', 'published_date']  # Adjust fields as needed

    # Additional validation (optional)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title
