from django.shortcuts import render
from home.models import ChatRoom
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request,group_name):
    return render(request,"index.html",{"group_name":group_name})

def test(request):
    if request.method=="POST":
        rName1=request.POST.get("rName")
        rCode1=request.POST.get("rCode")
        #print(rName1)
        #print(rCode1)
        mydata =ChatRoom.objects.filter(rName=rName1).values_list('rCode')
        x=mydata.get()
        if rCode1==x[0]:
            return redirect(f"chat/{rName1}")
        else:
            print(False)
    return render(request,"test.html")