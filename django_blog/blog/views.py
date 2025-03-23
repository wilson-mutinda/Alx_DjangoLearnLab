from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Custom registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else: 
            return render(request, 'blog/login.html', {'error': "Invalid username or password"})
    return render(request, 'blog/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile view
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/edit_profile.html')

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def  test_func(self):
        post = self.get_object()
        return self.request.user == post.author
