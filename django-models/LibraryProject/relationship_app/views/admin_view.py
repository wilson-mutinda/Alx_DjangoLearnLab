from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from relationship_app.models import UserProfile

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.ADMIN

@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin.html')
