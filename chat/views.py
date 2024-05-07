from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout # type: ignore
from .models import Profile

# Create your views here.
def login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('home/'+username)
    return render(request,'login.html')
def logout(request):
    authlogout(request)
    return redirect('login')
def chat(request):
    return render(request,'chat.html')

def home(request,user):
    userobj=User.objects.get(username=user)
    obj=Profile.objects.all().exclude(user=userobj)
    context={'users':obj}
    return render(request,'home.html',context)