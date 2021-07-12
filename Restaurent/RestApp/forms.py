from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.models import model_to_dict
from RestApp.models import Restaurents,Itemlist,User,Rolereq
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
class ReForm(forms.ModelForm):
    class Meta:
        model = Restaurents
        fields = fields = ["Rname","nitems","time","rsimg","address"]
        widgets = {
            "Rname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Restaurent Name",
            }),
            "nitems":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter number of items available",
            }),
            "time":forms.TimeInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Timings",
                "type":"time"
            }),
            "address":forms.Textarea(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Address",
                "rows":5,
            })
        }

class IForm(forms.ModelForm):
    class Meta:
        model=Itemlist
        fields=["rsid","Iname","Icategory","Iprice","Iavailability","Iimage"]
        widgets={
            "rsid":forms.Select(attrs={
                "class":"form-control my-2",
            }),
            "Iname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Item Name"
            }),
            "Icategory":forms.Select(attrs={
                "class":"form-control my-2",
                "placeholder":"Category"
            }),
            "Iprice":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter price"
            }),
            "Iavailability":forms.Select(attrs={
                "class":"form-control my-2",
            }),
            "Iimage":forms.FileInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Picture"
            })
        }

class UsgForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm Password"
    }))
    class Meta:
        model = User
        fields = ["first_name","last_name","age","email","username","mobilenumber","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control my-2",
            }),
            "age":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Age",
            })
        }
        
class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["uname","rltype","pfe"]
        widgets= {
            # "uname":forms.TextInput(attrs={
            #     "class":"form-control my-2",
            #     "readonly":True,
            # }),
            "rltype":forms.Select(attrs={
                "class":"form-control my-2",
                
            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets= {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class Pfupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","age","email","mobilenumber","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
                "readonly":True
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "uimg":forms.FileInput(attrs={
                "class":" my-2",
            }),
            "age":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Age",
            })
        }

class Chgepwd(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Old Password"
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter New Password"
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm New Password"
    }))
    class Meta:
        model = User
        fields =  ["old_password","new_password1","new_password2"]   
         