from django.shortcuts import render
from ..register.models import User
# Create your views here.
def faculty(request):
    user = User.objects.get(email=request.session['email'])
    context = {
        "user": user
    }
    return render(request, 'register/faculty_home.html', context)

def applypage(request):
	return render(request,'register/apply.html')

def checkapply(request):
	if request.method == "POST":
