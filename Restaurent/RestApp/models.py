
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(default=20)
    mobilenumber = models.CharField(max_length=10, null=True)
    uimg = models.ImageField(upload_to='ProfilePic/',default='bk.jpg')
    t = [(1,'Guest'),(2,'Manager'),(3,'User')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Manager'),(3,'User')]
    rltype = models.IntegerField(choices = f)
    pfe = models.ImageField(upload_to='Rolereqpics/',default='bk.jpg')
    is_checked = models.BooleanField(default=False)
    uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User, on_delete=models.CASCADE) 

class Restaurents(models.Model):
    Rname=models.CharField(max_length=30)
    nitems=models.IntegerField()
    time=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rsimg=models.ImageField(upload_to='RestaurentImages/',default='bk.jpg')
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Rname + " "+str(self.nitems)


class Itemlist(models.Model):
    cat=[
    ("select","Select Item Type"),
    ("veg","Veg"),
    ("non-veg","Non-Veg"),
    ]
    p=[('AV','Available'),('NA','Not Available'),('NA','Select Availability')]
    Iname=models.CharField(max_length=50)
    Icategory=models.CharField(max_length=50,choices=cat,default='select')
    Iprice=models.DecimalField(decimal_places=2,max_digits=10)
    Iavailability=models.CharField(max_length=50,choices=p,default='NA')
    Iimage=models.ImageField(upload_to='ItemImages/',default='bk.jpg')
    rsid = models.ForeignKey(Restaurents, on_delete=models.CASCADE)

