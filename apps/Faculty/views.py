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
		elif request.POST['leave_type']=="1": # Commuting Leave
			#return redirect('/') 		
			if user.n_commutingleave>0:
				user.n_commutingleave=user.n_commutingleave-1
				user.u_commutingleave=user.u_commutingleave+1
				user.save()
				context={
				"user":user
				"leave_type":"CommutingLeave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CommutingLeave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)		

		elif request.POST['leave_type']=="3":		#Special Casual Leave
			#return redirect('/') 		
			if user.n_specialleave>0:
				user.n_specialleave=user.n_specialleave-1
				user.u_specialleave=user.u_specialleave+1
				user.save()
				context={
				"user":user
				"leave_type":"Special Casual Leave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Special Casual Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)		
		elif request.POST['leave_type']=="4":		#Earn Leave
			#return redirect('/') 		
			if user.n_Earnleave>0:
				user.n_Earnleave=user.n_Earnleave-1
				user.u_Earnleave=user.u_Earnleave+1
				user.save()
				context={
				"user":user
				"leave_type":"Earn Leave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Earn Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)		
		elif request.POST['leave_type']=="5":		#Half Day Leave
			#return redirect('/') 		
			if user.n_halfleave>0:
				user.n_halfleave=user.n_halfleave-1
				user.u_halfleave=user.u_halfleave+1
				user.save()
				context={
				"user":user
				"leave_type":"Half Day Leave"
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Half Day Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)		