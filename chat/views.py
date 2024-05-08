from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout # type: ignore
from .models import Profile,Message
from django.db.models import Q # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore


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

@login_required(login_url='')
def chat(request,me,frnd):
    user=User.objects.get(username=me)
    friend=User.objects.get(username=frnd)
    user_obj=Profile.objects.get(user=user)
    frnd_obj=Profile.objects.get(user=friend)
    msg_obj=Message.objects.filter(Q(sender=user,receiver=friend) | Q(sender=friend,receiver=user)).order_by("date")
    context={
        'user':user,
        'friend':friend,
        'msg_obj':msg_obj,
        'user_obj':user_obj,
        'frnd_obj':frnd_obj
    }
    return render(request,'chat.html',context)

@login_required(login_url='')
def home(request,user):
    userobj=User.objects.get(username=user)
    profile=Profile.objects.get(user=userobj)
    obj=Profile.objects.all().exclude(user=userobj)
    context={'users':obj,'me':userobj,'profile':profile}
    return render(request,'home.html',context)

def signup(request):
    user=None
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        image=request.FILES['image']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        Profile.objects.create(name=name,phone=phone,user=user,image=image)
        return redirect('login')
    return render(request,'signup.html',{'user':user})