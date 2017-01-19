from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from pprint import pprint
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return HttpResponse("Hello, You are at the core index.")


def CreateUser(request):
    if request.method == 'GET':
        all_form = AllForm()

    if request.method == 'POST':
        # pprint(request.POST['last_name'])

        user = User.objects.create_user(username=request.POST['email'],
                                        email=request.POST['email'],
                                        password=request.POST['password'],
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name']
                                        )

        up = UserProfile()
        up.user = user
        up.gender = request.POST['gender']
        # up.first_name = request.POST['first_name']
        # up.last_name = request.POST['last_name']
        # pprint(request.POST['first_name'])
        # pprint(request.POST['last_name'])
        up.save()
        return  HttpResponse('You have been Successfully registered.')

    return render(request, 'register.html', { "all_form":all_form})

def login(request):
    login_form=LoginForm()
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            return HttpResponse('You have been Successfully logged.')
        else: return HttpResponse('some error occurred!')

    else: return render(request,"login.html",{"login_form":login_form})