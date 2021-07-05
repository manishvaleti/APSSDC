from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Restaurents(models.Model):
    Rname=models.CharField(max_length=30)
    nitems=models.IntegerField()
    time=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rsimg=models.ImageField(upload_to='RestaurentImages/',default='bk.jpg')
    
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
