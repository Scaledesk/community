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
      password = forms.CharField(max_length='15', widget=forms.PasswordInput())
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
       password = forms.CharField(max_length='15', widget=forms.PasswordInput())
       provideSupport=forms.CharField(max_length=300)
       needSupport=forms.CharField(max_length=300)
       PROFILE_TYPE = (("Startup Companies", "Startup Companies"), ("Mentors/Consultants", "Mentors/Consultants"),
                        ("Investors(Angels/VC Funds)", "Investors(Angels/VC Funds)"), ("Accelerators", "Accelerators")
                        , ("Incubators", "Incubators"), ("Event Manager", "Event Manager"))
       profileType = forms.ChoiceField(choices=PROFILE_TYPE)


class ProjectForm(forms.Form):
    companyName = forms.CharField(max_length=100)
    brandName = forms.CharField(max_length=100)
    BUSINESS_TYPE = (("B2B", "B2B"), ("B2C", "B2C"), ("C2B", "C2B"), ("B2B2C", "B2B2C"))
    typeOfBusiness = forms.ChoiceField(choices=BUSINESS_TYPE)
    url = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    logo = forms.ImageField(label='Select a file', help_text='max. 2 megabytes')
    videoLink = forms.CharField(max_length=256)
    aboutProductCompany = forms.FileField(label='Select a file', help_text='max. 2 megabytes')
    investor = forms.ImageField(label='Select a file', help_text='max. 2 megabytes')

class QuestionForm(forms.Form):
       question=forms.CharField(max_length=1000)