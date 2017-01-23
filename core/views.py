from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from pprint import pprint
from django.contrib.auth import authenticate, login
import json
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("Hello, You are at the core index.")


def CreateUser(request):
    if request.method == 'GET':
        register_form = Register()

    if request.method == 'POST':
        # response_data = {}

        #  if User.objects.filter(username=self.cleaned_data['email']).exists():

                email= request.POST['email']
                dipp = request.POST['dipp']
                pprint(dipp)

                try:
                    userData=UserDipp.objects.get(email=email,dipp=dipp)
                    pprint(userData)
                    if userData:
                        up = Profile()
                        up.companyName = request.POST['companyName']
                        up.designatePerson = request.POST['designatePerson']
                        up.founderCofounder = request.POST['founder']
                        up.website = request.POST['website']
                        up.mobile = request.POST['mobile']
                        up.address = request.POST['address']
                        up.city = request.POST['city']
                        up.state = request.POST['state']
                        up.pincode = request.POST['pincode']
                        up.facebook = request.POST['facebook']
                        up.linkedin = request.POST['linkedin']
                        up.twitter = request.POST['twitter']
                        up.industry = request.POST['industry']
                        up.save()

                    else: return HttpResponse("some error occurred!")

                except Exception as e:

                         return render(request, 'register.html', {"register": register_form})




    return render(request, 'register.html', { "register":register_form})






def login(request):
    login_form=LoginForm()
    if request.method=="POST":
        email=request.POST['email']
        dipp=request.POST['dipp']
        try:
            userData=UserDipp.objects.get(email=email,dipp=dipp)
            if userData:
                register = Register()
                return render(request, "register.html", {"register": register,'email':email,"dipp":dipp})

            else:
                return HttpResponse('some error occurred!')

        except Exception as e:


            return render(request, "login.html", {"login_form": login_form ,"msg": "Email/Dipp No. does not exist "})




    else: return render(request,"login.html",{"login_form":login_form})


  # if not userData :
  #              raise Http404("No MyModel matches the given query.")
  #
