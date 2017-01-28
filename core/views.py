from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from pprint import pprint
from django.contrib.auth import authenticate, login
from django.views.generic import RedirectView
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
from .models import *
# Create your views here.
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

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
                    return redirect("/dashboard")

                    # return   url(r'^.*/$', RedirectView.as_view(url='/home/'))
                    # return render(request, "dashboard.html", {"msg": "you have been successfully logged."})

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

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    return render(request, "dashboard.html",{'profile':profileData})

@login_required
def update(request):

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))

    if request.method == 'POST':
        try:
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

            # if
            # else:
            #     return render(request, "login.html",
            #                   {"login_form": login_form, "msg": "Email/Password. does not exist! "})
            #


        except Exception as e:

            return render(request, "profileUpdate.html", {"profile": profileData, "msg": e})


    else :return render(request, "profileUpdate.html",{'profile':profileData})

@login_required
def project(request):

    projectForm = ProjectForm()

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    if request.method=="POST":
          try:

              pro = Project()
              pro.profile=profileData
              pprint(profileData.companyName)
              logo = request.FILES['logo']
              aboutProductCompany = request.FILES['aboutProductCompany']
              pprint(aboutProductCompany)

              fs = FileSystemStorage()

              logo = fs.save(logo.name, logo)
              logo_url = fs.url(logo)
              fss = FileSystemStorage()
              aboutProductCompany = fss.save(aboutProductCompany.name, aboutProductCompany)
              aboutProductCompany_url = fss.url(aboutProductCompany)

              pro.brandName = request.POST['brandName']
              pro.typeOfBusiness = request.POST['typeOfBusiness']
              pro.url = request.POST['url']
              pro.description = request.POST['description']
              pro.logo = logo_url
              pro.videoLink = request.POST['videoLink']
              pro.aboutProductCompany = aboutProductCompany_url
              pro.investor = request.POST['investor']
              pro.save()
              return  render(request, "project.html", {"msg": "Project added successfully." ,"projectForm":projectForm})
          except Exception as e:
                return render(request, "project.html", {"msg":e ,"projectForm":projectForm})

    else :return render(request,"project.html",{"profile":profileData,"projectForm":projectForm})


@login_required
def QuestionView(request):
    questionForm=QuestionForm()
    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    if request.method == "POST":
       try:
           pro = Project()
           pro.profile = profileData
           ques=Question()
           ques.profile=profileData
           ques.question = request.POST['question']
           pro.save()
           ques.save()

           return render(request, "Question.html", {"msg": "Question added successfully.", "questionForm": questionForm})

       except Exception as e:

        return render(request, "Question.html",{"msg": e, "questionForm": questionForm})

    else : return render(request, "Question.html",{"questionForm": questionForm})


def AnswerView(request):

    # profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    questionData=Question.objects.all()
    #Data = Question.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    # for data in questionData:
    #  pprint(data.question)
    #  pprint(data.id)


    if request.method == 'GET':

        return render(request, "Answer.html", {"questionData": questionData})

    else:

        if request.method == "POST":
            try:
                # ques=Question()
                # ques.question=request.POST['id']
                ans=Answer()
                ans.answerField = request.POST['answer']
                ans.question=Question.objects.get(pk=request.POST['id'])
                ans.save()
                # ques.save()
                return render(request, "Answer.html",{"msg": "Answer  successfully submit.", "questionData": questionData})
            except Exception as e:
                 return render(request, "Answer.html",{"msg": e, "questionData": questionData})
        else:
            return render(request, "Answer.html")

