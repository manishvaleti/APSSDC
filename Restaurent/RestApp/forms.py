from django.forms import ModelForm
from RestApp.models import Restaurents
from django import forms
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