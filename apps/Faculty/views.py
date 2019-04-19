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
		#email=request.session['email']
		user = User.objects.get(email=request.session['email'])
		if user.n_compleaves>0:
			user.n_casualleaves=user.n_compleaves-1
			user.u_casualleave=user.u_casualleave+1
			user.save(['n_casualleaves','u_casualleave'])
			return 


