from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

def logout(request):
    if request.session['email'] is not None:
        request.session['email'] = None
        request.session['LoggedIn']=False

    return redirect('/')


def index(request):
    return render(request, 'register/index.html')

def register(request):
    """
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    """
    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(user_type=request.POST['user_type'],first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['email'] = user.email
    context={
        "user":user
    }
    return render(request,'register/success.html',context)

def login(request):
    request.session['email']=None
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['email'] = user.email
            request.session['LoggedIn'] = True
            if user.user_type == "faculty":
                return redirect('/faculty')
            elif user.user_type == "hod":
                return redirect('/hod')
            elif user.user_type == "director":
                return redirect('/director')         
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)