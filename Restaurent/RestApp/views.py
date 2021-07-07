from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,IForm, Rltype,UsgForm
from RestApp.models import Itemlist, Restaurents
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')
@login_required
def restlist(request):
    y=Restaurents.objects.filter(uid_id=request.user.id)
    if request.method =="POST":
        t = ReForm(request.POST,request.FILES)
        if t.is_valid():
            c = t.save(commit=False)
            c.uid_id= request.user.id
            c.save()
            t.save()
            messages.success(request,"Restaurent Added Successfully")
            return redirect('/rlist')
    t = ReForm(request.FILES)
    return render(request,'app/restlist.html',{'q':t,'a':y})
@login_required
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
@login_required
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

def vx(request):
    s=Restaurents.objects.filter(uid_id=request.user.id)
    return render(request,'app/v.html',{"a":s})
@login_required
def itlist(request):
    st = list(Restaurents.objects.filter(uid_id=request.user.id))
    mm = Itemlist.objects.all()
    d,i={},0
    for mp in mm:
        for h in st:
            if h.id == mp.rsid_id:
                d[i] = mp.Iname,mp.Icategory,mp.Iprice,mp.Iimage,mp.Iavailability,mp.id,h.Rname
                i=i+1

    # y=Itemlist.objects.all()
    if request.method == "POST":
        k = IForm(request.POST,request.FILES)
        if k.is_valid():
            n=k.save(commit=False)
            n.save()
            messages.success(request,'{} Item is Added successfully'.format(n.Iname))
            return redirect('/ilist/')
    k=IForm()
    return render(request,'app/itmlist.html',{'r':k,'er':st,'a':d.values()})

def usrreg(request):
    if request.method=="POST":
        d = UsgForm(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d = UsgForm()
    return render(request,'app/usrregister.html',{'t':d})

def itup(request,m):
    k=Itemlist.objects.get(id=m)
    if request.method=="POST":
        e=IForm(request.POST,request.FILES,instance=k)
        if e.is_valid():
            e.save()
            messages.warning(request,"{} Restaurent Updated Successfully".format(k.Iname))
            return redirect('/ilist')
    e=IForm(instance=k)
    return render(request,'app/itupdate.html',{'x':e})

def itdel(request,m):
    r=Itemlist.objects.get(id=m)
    if request.method=="POST":
        r.delete()
        messages.success(request,"{} Restaurent Deleted Successfully".format(r.Iname))
        return redirect('/ilist')
    e=IForm(instance=r)
    return render(request,'app/itdel.html',{'a':e})
def ivw(request,a):
    s=Itemlist.objects.get(id=a)
    return render(request,'app/iview.html',{'z':s})
@login_required
def rolereq(request):
    k = Rltype()
    return render(request,'app/rolereq.html',{'d':k})

@login_required
def gveperm(request):
    return render(request,'app/gvper.html')