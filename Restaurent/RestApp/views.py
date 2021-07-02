from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.models import Restaurents
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def restlist(request):
    y=Restaurents.objects.all()
    if request.method =="POST":
        t = ReForm(request.POST,request.FILES)
        if t.is_valid():
            t.save()
            messages.success(request,"Restaurent Added Successfully")
            return redirect('/rlist')
    t = ReForm(request.FILES)
    return render(request,'app/restlist.html',{'q':t,'a':y})

def rstup(request,m):
    k=Restaurents.objects.get(id=m)
    if request.method=="POST":
        e=ReForm(request.POST,request.FILES,instance=k)
        if e.is_valid():
            e.save()
            messages.warning(request,"{} Restaurent Updated Successfully".format(k.Rname))
            return redirect('/rlist')
    e=ReForm(instance=k)
    return render(request,'app/restupdate.html',{'x':e})

def rstdel(request,m):
    r=Restaurents.objects.get(id=m)
    if request.method=="POST":
        r.delete()
        messages.success(request,"{} Restaurent Deleted Successfully".format(r.Rname))
        return redirect('/rlist')
    e=ReForm(instance=r)
    return render(request,'app/rstdel.html',{'a':e})

def rstvw(request,a):
    s=Restaurents.objects.get(id=a)
    return render(request,'app/restview.html',{'z':s})

def v(request):
    s=Restaurents.objects.all()
    return render(request,'app/v.html',{"a":s})