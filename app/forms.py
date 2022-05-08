from dataclasses import fields
from django import forms
from .models import *

usertype = [("Admin","admin"),("Bloodbank","bloodbank")]
class UserForm(forms.ModelForm):
    firstname=forms.CharField()
    lastname=forms.CharField()
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    usertype=forms.CharField(widget=forms.Select(choices=usertype))
    class Meta:
        model = MyUser
        fields="__all__"

class BBForm(forms.ModelForm):
    class Meta:
        model = Bloodbank
        fields="__all__"

class DForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields="__all__"

class RForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields="__all__"

class CForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields="__all__"