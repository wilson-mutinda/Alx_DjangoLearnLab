from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # ✅ Display author's username

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # ✅ Display author's username
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # ✅ Allow setting post ID

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
