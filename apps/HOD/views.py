from django.shortcuts import render
from ..register.models import User
from ..Faculty.models import Leaves
# Create your views here.
def hod(request):
	if request.session['email'] != None:
	    user = User.objects.get(email=request.session['email'])
	    context = {
	        "user": user
	    }
	    return render(request, 'register/hod_home.html', context)
	else:	
		return redirect('/')


def approvepage(request):
	leave=Leaves.objects.all()
	"""l1=[]
				for l in leave:
					l1.append(l.email)
				print(l1)	"""

	context={
	"Leaves":leave
	}
	return render(request,"register/approve.html",context)
from datetime import datetime
#from dateutil.parser import parse
def singledetails(request):
	#if request.method=='POST' and User.objects.get(email=request.POST['email']):

	if request.POST.get('Accept'):

		email=request.POST.get('email')
		lt=request.POST.get('Type')
		fd=request.POST.get('fromdate')
		td=request.POST.get('todate')
		l=Leaves.objects.get(email=email,leave_type=lt)
		l.status=2
		l.save()
		return render(request,"register/hod_home.html") 
		#return render(request,"register/singleapprove.html",context)
	else:
		email=request.POST.get('email')
		lt=request.POST.get('Type')
		fd=request.POST.get('fromdate')
		td=request.POST.get('todate')
		l=Leaves.objects.get(email=email,leave_type=lt)
		l.status=0
		l.save()
		return render(request,"register/hod_home.html")
		
