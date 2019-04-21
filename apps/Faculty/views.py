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
		#print (request)
		user = User.objects.get(email=request.session['email'])
		print(request.POST['leave_type'])
		if request.POST['leave_type']=="2":
			#return redirect('/') 		
			if user.n_casualleave>0 and user.a_casualleave<30:
				#user.n_casualleave=user.n_casualleave-1
				user.a_casualleave=user.a_casualleave+1
				user.save()
				l="CasualLeave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CasualLeave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				#print("Entered and succeded")
				return render(request,'register/successapply.html',context)
		elif request.POST['leave_type']=="1": # Commuting Leave
			#return redirect('/') 		
			if user.n_commutingleave>0 and user.a_commutingleave<30:
				#user.n_commutingleave=user.n_commutingleave-1
				user.a_commutingleave=user.u_commutingleave+1
				user.save()
				l="CommutingLeave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="CommutingLeave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)		

		elif request.POST['leave_type']=="3":		#Special Casual Leave
			if user.n_specialleave>0:
				#user.n_specialleave=user.n_specialleave-1
				user.a_specialleave=user.a_specialleave+1
				user.save()
				l="Special Casual Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Special Casual Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)		
		elif request.POST['leave_type']=="4":		#Earn Leave
			if user.n_Earnleave>0:
				#user.n_Earnleave=user.n_Earnleave-1
				user.a_Earnleave=user.a_Earnleave+1
				user.save()
				l="Earn Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Earn Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)		
		elif request.POST['leave_type']=="5":		#Half Day Leave
			if user.n_halfleave>0:
				#user.n_halfleave=user.n_halfleave-1
				user.a_halfleave=user.a_halfleave+1
				user.save()
				l="Half Day Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Half Day Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)
		elif request.POST['leave_type']=="6":		#Duty Leave
			if user.n_dutyleave>0:
				#user.n_dutyleave=user.n_dutyleave-1
				user.a_dutyleave=user.a_dutyleave+1
				user.save()
				l="Duty Leave"
				context={
				"user":user,
				"leavetype":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Duty Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)
		elif request.POST['leave_type']=="7":		#Sick Leave
			if user.n_sickleave>0:
				#user.n_sickleave=user.n_sickleave-1
				user.a_sickleave=user.a_sickleave+1
				user.save()
				l="Sick Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Sick Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)						
		elif request.POST['leave_type']=="8":		#Maternity Leave 
			if user.n_maternityleave>0:
				#user.n_maternityleave=user.n_maternityleave-1
				user.a_maternityleave=user.a_maternityleave+1
				user.save()
				l="Maternity Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Special Casual Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'],status=3)	
				leave.save()
				return render(request,'register/successapply.html',context)
		elif request.POST['leave_type']=="9":		#Paternity Leave
			if user.n_paternityleave>0:
				#user.n_paternityleave=user.n_paternityleave-1
				user.a_paternityleave=user.a_paternityleave+1
				user.save()
				l="Paternity Leave"
				context={
				"user":user,
				"leave_type":l
				}
				leave=Leaves.objects.create(email=request.session['email'],leave_type="Special Casual Leave",from_date=request.POST['fromdate'],to_date=request.POST['todate'])	
				leave.save()
				return render(request,'register/successapply.html',context)
									