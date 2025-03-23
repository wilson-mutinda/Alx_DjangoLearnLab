from django import forms
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

class PostForm(forms.ModelForm):
    tags = TagField(required=False, widget=TagWidget())  # Use TagWidget explicitly

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'})
        }
