from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from relationship_app.models import UserProfile

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.LIBRARIAN

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')
