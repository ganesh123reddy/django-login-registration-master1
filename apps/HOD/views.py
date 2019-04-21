from django.shortcuts import render
from ..register.models import User
# Create your views here.
def hod(request):
	return render(request,"register/hod_home.html")


def approvepage(request):
	return render(request,"register/singleapprove.html")

def approvecheck(request):
	return -1