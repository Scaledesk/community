# from django.db import models
# from django.forms import ModelForm
from django import forms
from core.models import *
from django.contrib.auth.models import User

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['gender', 'age']
#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username']


class AllForm(forms.Form):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    email = forms.EmailField()
    password = forms.CharField(max_length='15',widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length='15', widget=forms.PasswordInput())

class LoginForm(forms.Form):
      email=forms.EmailField()
      dipp=forms.CharField(max_length="15")
class Register (forms.Form) :
       email = forms.EmailField()
       dipp = forms.CharField(max_length="15")
       companyName = forms.CharField(max_length=100)
       designatePerson = forms.CharField(max_length=50)
       founderCofounder = forms.CharField(max_length=50)
       website = forms.CharField(max_length=50)
       mobile = forms.IntegerField()
       address = forms.CharField(max_length=256)
       city = forms.CharField(max_length=25)
       state = forms.CharField(max_length=30)
       pincode = forms.IntegerField()
       facebook = forms.CharField(max_length=256)
       linkedin = forms.CharField(max_length=256)
       twitter = forms.CharField(max_length=256)
       industry = forms.CharField(max_length=100)
