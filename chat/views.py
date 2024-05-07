from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout # type: ignore
from .models import Profile,Message
from django.db.models import Q # type: ignore

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

def home(request,user):
    userobj=User.objects.get(username=user)
    obj=Profile.objects.all().exclude(user=userobj)
    context={'users':obj,'me':userobj}
    return render(request,'home.html',context)