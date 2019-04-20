from django.shortcuts import render
from ..register.models import User
from django.shortcuts import render, HttpResponse, redirect
from .models import Leaves
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
		print(request.POST['leave_type'])
		if request.POST['leave_type']=="2":
			#return redirect('/') 		
			if user.n_casualleaves>0:
				user.n_casualleaves=user.n_casualleaves-1
				user.u_casualleave=user.u_casualleave+1
				user.save(['n_casualleaves','u_casualleave'])
				context={
				"user":user
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CasualLeaves",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/Success.html',context)
		else:
			return redirect('/')
				

