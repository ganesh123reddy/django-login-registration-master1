from django.shortcuts import render
from ..register.models import User
from ..Faculty.models import Leaves
# Create your views here.
def hod(request):
	return render(request,"register/hod_home.html")

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

def approvecheck(request):
	return -1

