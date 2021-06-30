from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm
from RestApp.models import Restaurents
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
        t = ReForm(request.POST)
        if t.is_valid():
            t.save()
            return redirect('/rlist')
    t = ReForm()
    return render(request,'app/restlist.html',{'q':t,'a':y})

def rstup(request,m):
    k=Restaurents.objects.get(id=m)
    if request.method=="POST":
        e=ReForm(request.POST,instance=k)
        if e.is_valid():
            e.save()
            return redirect('/rlist')
    e=ReForm(instance=k)
    return render(request,'app/restupdate.html',{'x':e})

def rstdel(request,m):
    r=Restaurents.objects.get(id=m)
    if request.method=="POST":
        r.delete()
        return redirect('/rlist')
    e=ReForm(instance=r)
    return render(request,'app/rstdel.html',{'a':e})
