from django.shortcuts import render
from ..register.models import User
from ..Faculty.models import Leaves
import datetime
# Create your views here.
def director(request):
	if request.session['email'] != None:
	    user = User.objects.get(email=request.session['email'])
	    context = {
	        "user": user
	    }
	    if user.
	    return render(request, 'register/director_home.html', context)
	else:	
		return redirect('/')


def approvepage_dir(request):
	#print("*********************************************")
	leave=Leaves.objects.all()
	context={
	"Leaves":leave
	}
	return render(request,"register/approve1.html",context)



#from dateutil.parser import parse
def singledetails_dir(request):
	#if request.method=='POST' and User.objects.get(email=request.POST['email']):
	print("*********************************************")
	if request.POST.get('Accept'):
		email=request.POST.get('email')
		lt=request.POST.get('Type')
		fd=request.POST.get('fromdate')
		td=request.POST.get('todate')
		l=Leaves.objects.get(email=email,leave_type=lt)
		l.status=1
		l.save()
		return render(request,"register/director_home.html") 
		#return render(request,"register/singleapprove.html",context)
	else:
		email=request.POST.get('email')
		lt=request.POST.get('Type')
		fd=request.POST.get('fromdate')
		td=request.POST.get('todate')
		l=Leaves.objects.get(email=email,leave_type=lt)
		l.status=0
		l.save()
		return render(request,"register/director_home.html")

