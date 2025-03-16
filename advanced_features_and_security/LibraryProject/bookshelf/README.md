# Django Permissions & Groups Setup

## 1. Model Permissions
- `can_view`: View books
- `can_create`: Add books
- `can_edit`: Edit books
- `can_delete`: Delete books

## 2. User Groups
- **Viewers**: Only `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

## 3. View Protection
- **book_list** → `@permission_required('books.can_view')`
- **add_book** → `@permission_required('books.can_create')`
- **edit_book** → `@permission_required('books.can_edit')`
- **delete_book** → `@permission_required('books.can_delete')`

## 4. Setup Instructions
1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
