from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.models import model_to_dict
from RestApp.models import Restaurents,Itemlist
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ReForm(forms.ModelForm):
    class Meta:
        model = Restaurents
        fields = "__all__"
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
        fields="__all__"
        widgets={
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
        fields = ["username"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            })
        }