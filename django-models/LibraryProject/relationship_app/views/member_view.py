from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from relationship_app.models import UserProfile

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.MEMBER

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member.html')
