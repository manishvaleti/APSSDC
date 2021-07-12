from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,IForm, Rltype, Rlupd,UsgForm,Pfupd,Chgepwd
from RestApp.models import Itemlist, Restaurents, Rolereq, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Restaurent import settings
from django.core.mail import send_mail
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
    t = Restaurents.objects.all()
    return render(request,'app/v.html',{"a":s,"y":t})
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
        d = UsgForm(request.POST,request.FILES)
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
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k =Rltype(request.POST,request.FILES)
        if k.is_valid:
            y = k.save(commit = False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            y.save()
            return redirect('/')
    k = Rltype()
    return render(request,'app/rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d = {}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id:
                continue
            else:
                d[m.id] = n.username,m.rltype,n.role,n.id,m.id
    return render(request,'app/gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y=Rolereq.objects.get(ud_id=t)
    d=User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            #d.role = s.rltype
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'app/gvepermissions.html',{'c':n})
@login_required
def pfle(request):
    x = User.objects.get(id=request.user.id)
    return render(request,'app/profile.html',{'d':x})

@login_required
def feedback(request):
    if request.method == "POST":
        sd = request.POST['snmail'].split(',')
        sm = request.POST['sub']
        mg = request.POST['msg']
        rt = settings.EMAIL_HOST_USER
        dt = send_mail(sm,mg,rt,sd)
        if dt == 1:
            return redirect('/')
    return render(request,'app/feedback.html')

@login_required
def reqdel(request,t):
    r = Rolereq.objects.get(id=t)
    u = User.objects.get(id=r.ud_id)
    if request.method == "POST":
        u.role=1
        r.delete()
        u.save()
        messages.success(request,"Request from {} Deleted Successfully".format(u.username))
        return redirect('/gvper')
    return render(request,'app/reqdel.html',{'a':u})

@login_required
def pfupd(request):
    d=User.objects.get(id=request.user.id)
    if request.method=="POST":
        pf=Pfupd(request.POST,request.FILES,instance=d)
        if pf.is_valid():
            pf.save()
            return redirect('/pfle')
    pf=Pfupd(instance=d)
    return render(request,'app/pfleupdate.html',{'u':pf})

@login_required
def changepwd(request):
    if request.method == "POST":
        k = Chgepwd(user=request.user,data=request.POST)
        if k.is_valid():
            k.save()
            return redirect('/login')
    k = Chgepwd(user=request)
    return render(request,'app/changepwd.html',{'t':k})