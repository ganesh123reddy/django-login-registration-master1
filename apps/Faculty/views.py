from django.shortcuts import render
from ..register.models import User
# Create your views here.
def faculty(request):
    user = User.objects.get(email=request.User.email)
    context = {
        "user": user
    }
    return render(request, 'faculty/faculty_home.html', context)