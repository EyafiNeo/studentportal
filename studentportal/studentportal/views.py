import imp
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from profileapp.models import *
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')



def log_in(request):
    if request.method == "POST":
        loginUsername = request.POST['uname']
        loginPassword = request.POST['psw']
        user = authenticate(username = loginUsername, password = loginPassword)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            
        else:
            messages.error(request,"Enter Valid Username or Password")
            return redirect('login')
    else:
        return render(request,'index.html')



@login_required
def log_out(request):
    logout(request)
    return redirect('/')



def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        obj = paymentdesc.objects.get(user = user)
        obj2 = sgpadashboard.objects.get(user = user)
        return render(request,'dashboard.html',{'user':user,'payment':obj,'sgpa':obj2})
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login')

def results(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            studentid = request.POST['studid']
            semester = request.POST['semester']
            obj = result.objects.filter(semester = semester).filter(studentid = studentid).values()
            obj2 = cgpa.objects.get(semestername = semester,student_id = studentid)
            user = request.user
            print(obj2)
            return render(request,'result.html',{'result':obj,'cgpa':obj2,'user':user})
    
        return render(request,'result.html')
    else:
        return redirect('login')