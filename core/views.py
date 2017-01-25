from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from pprint import pprint
from django.contrib.auth import authenticate, login
from django.views.generic import RedirectView
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from .models import *
# Create your views here.
from django.contrib import auth
def index(request):
    return HttpResponse("Hello, You are at the core index.")


def CreateUser(request):
    if request.method == 'GET':
        register_form = Register()

    if request.method == 'POST':


        #  if User.objects.filter(username=self.cleaned_data['email']).exists():

                email= request.POST['email']
                dipp = request.POST['dipp']
                password=request.POST['password']
                response_data = {}
                # pprint(dipp)

                try:
                    userData=UserDipp.objects.get(email=email,dipp=dipp)
                    # pprint(userData.email)
                    # pprint(userData.dipp)

                    if str(userData.dipp) == str(dipp):
                        user = User.objects.create_user(email, email, password)
                        # pprint(userData.dipp)
                        # pprint(userData.email)
                        up = Profile()
                        up.userdipp=userData
                        # up.Profile.object(status=1)
                        # up.profile = userData
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
                        userData.status=1
                        userData.user=user
                        userData.save()
                        response_data['result'] = 'Your profile has been created successfully!'
                        return HttpResponse(
                            json.dumps(response_data),
                            content_type="application/json"
                        )

                    else:  return HttpResponse(
                                       json.dumps({"result": "Email and Dipp No. does not exist"}),
                                       content_type="application/json"
                                          )

                except Exception as e:

                    return HttpResponse(
                        json.dumps({"result": 'Email and Dipp No. does not exist'}),
                        content_type="application/json"
                    )


    return render(request, 'register.html', { "register":register_form})






def login(request):
    login_form=LoginForm()
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        pprint(email)
        pprint(password)
        try:
            user = authenticate(username=email, password=password)
            if user is not None:
                # if user.is_active:
                    auth.login(request, user)
                    # return HttpResponseRedirect("/new_url/")

                    # return   url(r'^.*/$', RedirectView.as_view(url='/home/'))
                    return render(request, "dashboard.html", {"msg": "you have been successfully logged."})

                # else:  return render(request, "login.html", {"login_form": login_form ,"msg": "disabled account "})

            else:  return render(request, "login.html", {"login_form": login_form ,"msg": "Email/Password. does not exist! "})



        except Exception as e:


            return render(request, "login.html", {"login_form": login_form ,"msg": e})




    else: return render(request,"login.html",{"login_form":login_form})


  # if not userData :
  #              raise Http404("No MyModel matches the given query.")
  #
@login_required
def dashboard(request):

    return render(request, "dashboard.html")