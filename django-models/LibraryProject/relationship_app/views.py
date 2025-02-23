from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Library
from .models import Author, Book, Librarian, UserProfile
from .forms import BookForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Update with the actual book listing page
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

def is_admin(user):
    return user.is_authenticated and getattr(user, 'userprofile', None) and user.userprofile.role == 'Admin'


def is_librarian(user):
    try:
        return user.userprofile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False

def is_member(user):
    try:
        return user.userprofile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False

@login_required
@user_passes_test(is_admin, login_url='/login')
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member.html')

def list_all_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "request_app/login.html", {'form': form})

def user_logout(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {'form': form})
