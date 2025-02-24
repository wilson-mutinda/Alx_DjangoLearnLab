from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in the list view
    search_fields = ('title', 'author')  # Allow searching by title and author
    list_filter = ('publication_year',)  # Add filter for publication year

def setup_permissions():
    """Function to create groups and assign permissions"""
    book_content_type = ContentType.objects.get_for_model(Book)

    # Create Permissions if they don't exist
    can_view, _ = Permission.objects.get_or_create(
        codename='can_view',
        content_type=book_content_type,
        defaults={'name': 'Can View Book'}
    )
    can_create, _ = Permission.objects.get_or_create(
        codename='can_create',
        content_type=book_content_type,
        defaults={'name': 'Can Create Book'}
    )
    can_edit, _ = Permission.objects.get_or_create(
        codename='can_edit',
        content_type=book_content_type,
        defaults={'name': 'Can Edit Book'}
    )
    can_delete, _ = Permission.objects.get_or_create(
        codename='can_delete',
        content_type=book_content_type,
        defaults={'name': 'Can Delete Book'}
    )

    # Create groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions to groups
    editors.permissions.add(can_view, can_create, can_edit)
    viewers.permissions.add(can_view)
    admins.permissions.add(can_view, can_create, can_edit, can_delete)

# Run setup_permissions only after migrations are applied
import django
from django.core.management import call_command

if django.apps.apps.ready:
    try:
        call_command("migrate")  # Ensure migrations are applied
        setup_permissions()
    except Exception as e:
        print(f"Error setting up permissions: {e}")
