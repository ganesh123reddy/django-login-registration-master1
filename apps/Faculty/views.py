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
	#if True:
		#email=request.session['email']
	if request.session['email'] is not None:
	#return render(request,'register/successapply.html')
		print (request)
		user = User.objects.get(email=request.session['email'])
		print(request.POST['leave_type'])
		if request.POST['leave_type']=="2":
			#return redirect('/') 		
			if user.n_casualleave>0:
				user.n_casualleave=user.n_casualleave-1
				user.u_casualleave=user.u_casualleave+1
				user.save()
				context={
				"user":user
				"leave_type":"CasualLeave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CasualLeave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)
		if request.POST['leave_type']=="1":
			#return redirect('/') 		
			if user.n_casualleave>0:
				user.n_casualleave=user.n_leave-1
				user.u_casualleave=user.u_leave+1
				user.save()
				context={
				"user":user
				"leave_type":"CasualLeave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CasualLeave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)		

