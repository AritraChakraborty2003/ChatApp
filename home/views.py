from django.shortcuts import render
from home.models import ChatRoom
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
@login_required(login_url="main")
def index(request,group_name):
    return render(request,"index.html",{"group_name":group_name})

def test(request):
    if request.method=="POST":
        rName1=request.POST.get("rName")
        email1=request.POST.get("email")
        rCode1=request.POST.get("rCode")
        #print(rName1)
        #print(rCode1)
        user=authenticate(request,username=rName1,password=rCode1)
        if user is not None:
         mydata =ChatRoom.objects.filter(rName=rName1).values_list('rCode')
         x=mydata.get()
         if rCode1==x[0]:
          login(request,user)
          return redirect(f"chat/{rName1}")
         else:
            return HttpResponse("Value Error...")
        else:
            return HttpResponse("Invalid username or password")
        
    return render(request,"test.html")
def logout(request,group_name):
    logouts(request)
    return redirect("main")