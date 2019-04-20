from django.shortcuts import render
from ..register.models import User
from django.shortcuts import render, HttpResponse, redirect
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
	if True:
		#email=request.session['email']
		user = User.objects.get(email=request.session['email'])
		if request.POST['leave_type']==2:
			if user.n_compleaves>0:
				user.n_casualleaves=user.n_compleaves-1
				user.u_casualleave=user.u_casualleave+1
				user.save(['n_casualleaves','u_casualleave'])
				context={
				"user":user
				}
				#print("Entered and succeded")
				return render(request,'register/faculty_home.html',context)
		else:
			return redirect('/')
				

