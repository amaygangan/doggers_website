from django import forms
from blogapp1.models import Doginfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class empformclass(forms.Form):
    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    department=forms.CharField(max_length=50)
    doj=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))

class Doginfoclass(forms.ModelForm):
    
    breed_name=forms.CharField(max_length=50)
    gender=forms.IntegerField()
    age=forms.IntegerField()
    vaccine=forms.CharField(max_length=40)
    price=forms.IntegerField()
    uid=forms.IntegerField()

    class Meta:
        model=Doginfo
        fields=["breed_name","gender","age","vaccine","price","uid"]

class UserRegister(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
