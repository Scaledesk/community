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
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage


def index(request):
    return HttpResponse("Hello, You are at the core index.")

def Signup(request):
    if request.method == 'POST':
       response_data = {}
       email = request.POST['email']
       dipp = request.POST['dipp']
       try:
           userData = UserDipp.objects.get(email=email, dipp=dipp)
           # return redirect("/register")
           request.session['email'] = email
           request.session['dipp'] = dipp
           response_data['success'] = '/register'
           return HttpResponse(
               json.dumps(response_data),
               content_type="application/json"
           )

       except Exception as e:

           response_data['error'] = 'Your Email and Dipp not valid!'
           return HttpResponse(
               json.dumps(response_data),
               content_type="application/json"
           )

    return render(request,'signup.html')

# @login_required(login_url="/login/")
def CreateUser(request):
    register_form = Register({"dipp":request.session.get('dipp'), "email":request.session.get('email')})


    if request.method == 'POST':


                                        #
                    # post = form.save(commit=False)

                    #  if User.objects.filter(username=self.cleaned_data['email']).exists():



                    email= request.POST['email']
                    dipp = request.POST['dipp']
                    password=request.POST['password']
                    # pprint(registerData)
                    # response_data = {}
                    # pprint(dipp)
                    # pprint(email)
                    try:
                            userData = UserDipp.objects.get(email=email, dipp=dipp)
                        # pprint(userData.dipp)

                        # if str(userData.dipp) == str(dipp):

                            user = User.objects.create_user(email, email, password)
                            # pprint(data)
                            # pprint(userData.dipp)
                            # pprint(userData.email)
                            up = Profile()
                            up.userdipp=userData
                            # up.Profile.object(status=1)
                            # up.profile = userData
                            userData.status=1
                            userData.user=user
                            userData.save()

                            data = request.POST

                            processed_data = {}


                            for k in data:
                                processed_data.update({k: (data[k])})
                            for k in up._meta.fields:
                                if k.column in processed_data:
                                    if not k.column is 'id':
                                        setattr(up, k.column, processed_data[k.column])
                            # import ipdb;ipdb.set_trace();
                            up.save()

                            user = authenticate(username=email, password=password)
                            auth.login(request, user)

                            return redirect('/project/')


                    except Exception as e:
                        return render(request, 'register.html',{"result": "your profile has been already registered","register":register_form})



    return render(request, 'register.html',{"register":register_form})






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
@login_required(login_url="/login/")
def dashboard(request):

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    return render(request, "dashboard.html",{'profile':profileData})

@login_required(login_url="/login/")
def update(request):

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    response_data = {}
    updateProfile = Register({"companyName":profileData.companyName, "designatePerson":profileData.designatePerson, "founderCofounder":profileData.founderCofounder,
                              "website":profileData.website, "mobile":profileData.mobile, "address":profileData.address
                                 , "city": profileData.city, "state":profileData.state, "pincode":profileData.pincode
                                 , "facebook": profileData.facebook, "linkedin":profileData.linkedin, "twitter":profileData.twitter
                                 , "industry": profileData.industry, "provideSupport":profileData.provideSupport, "needSupport":profileData.needSupport})

    if request.method == 'POST':
        try:
            up=profileData

            data = request.POST

            processed_data = {}

            for k in data:
                processed_data.update({k: (data[k])})
            for k in up._meta.fields:
                if k.column in processed_data:
                    if not k.column is 'id':
                        setattr(up, k.column, processed_data[k.column])
            # import ipdb;ipdb.set_trace();
            up.save()

            return render(request, "profileUpdate.html", {'profile':updateProfile,"result": "Your profile has been Updated successfully"})


        except Exception as e:

            return render(request, "profileUpdate.html", {"profile": profileData, "msg": e})


    else :return render(request, "profileUpdate.html",{'profile':updateProfile})

@login_required(login_url="/login/")
def project(request):

    # import ipdb;  ipdb.set_trace()

    profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
    projectForm = ProjectForm({'companyName':profileData.companyName})

    if request.method=="POST":
          try:

              pro = Project()
              pro.profile=profileData
              # pprint(profileData.companyName)
              logo = request.FILES['logo']
              investor = request.FILES['investor']
              aboutProductCompany = request.FILES['aboutProductCompany']

              fs = FileSystemStorage()

              logo = fs.save(logo.name, logo)
              logo_url = fs.url(logo)
              fss = FileSystemStorage()

              investor = fss.save(investor.name, investor)
              investor_url = fss.url(investor)


              fsss = FileSystemStorage()

              aboutProductCompany = fsss.save(aboutProductCompany.name, aboutProductCompany)
              aboutProductCompany_url = fsss.url(aboutProductCompany)



              pro.brandName = request.POST['brandName']
              pro.typeOfBusiness = request.POST['typeOfBusiness']
              pro.url = request.POST['url']
              pro.description = request.POST['description']
              pro.logo = logo_url
              pro.videoLink = request.POST['videoLink']
              pro.aboutProductCompany = aboutProductCompany_url
              pro.investor = investor_url
              pro.save()
              return redirect("/dashboard/")
          except Exception as e:
                return render(request, "project.html", {"msg":e ,"projectForm":projectForm})

    else :return render(request,"project.html",{"profile":profileData,"projectForm":projectForm})


@login_required(login_url="/login/")
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


# def AnswerView(request):
#     ans = Answer()
#
#     # profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))
#
#     questionData=Question.objects.all()
#
#     # data = Question.objects.get(pk=Answer.objects.get(ans.answerField))
#     for data1 in questionData:
#
#         data = Answer.objects.filter(question=data1)
#
#         pprint(data)
#
#
#     # for data1 in data:
#     #
#     #  pprint(data1)
#
#
#
#     if request.method == 'GET':
#
#         return render(request, "Answer.html", {"questionData": questionData})
#
#     else:
#
#         if request.method == "POST":
#             try:
#                 # ques=Question()
#                 # ques.question=request.POST['id']
#
#                 ans.answerField = request.POST['answer']
#                 ans.question=Question.objects.get(pk=request.POST['id'])
#                 ans.save()
#                 # ques.save()
#                 return render(request, "Answer.html",{"msg": "Answer  successfully submit.", "questionData": questionData})
#             except Exception as e:
#                  return render(request, "Answer.html",{"msg": e, "questionData": questionData})
#         else:
#             return render(request, "Answer.html")
#


# @login_required(login_url="/login/")
def AnswerView(request):
    ans = Answer()

    # profileData = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user))

    questionData=Question.objects.all()
    ansData = Answer.objects.all()

    # userdippno = Question.objects.get(profile = Profile.objects.get(userdipp=UserDipp.objects.get(user=request.user)))
    # userdipp = UserDipp.objects.get(user=request.user)
    # pprint(userdippno)

    # data = Question.objects.get(pk=Answer.objects.get(ans.answerField))
    # for data1 in questionData:
    #
    #     data = Answer.objects.filter(question=data1)

        # pprint(data[0].question.question)
        # pprint(data1.question)
        # for obj in data:
        #
        #     pprint(obj.answerField)

    # for data1 in data:
    #
    #  pprint(data1)



    if request.method == 'GET':

        return render(request, "Answer.html", {"questionData": questionData, "ansData":ansData})

    else:

        if request.method == "POST":
            try:
                # ques=Question()
                # ques.question=request.POST['id']

                ans.answerField = request.POST['answer']
                ans.question=Question.objects.get(pk=request.POST['id'])
                ans.save()
                # ques.save()
                return render(request, "Answer.html",{"msg": "Answer  successfully submit.", "questionData": questionData, "ansData":ansData})
            except Exception as e:
                 return render(request, "Answer.html",{"msg": e, "questionData": questionData, "ansData":ansData})
        else:
            return render(request, "Answer.html",{"questionData": questionData, "ansData":ansData})





def AnswerDelete(request, id):
    pprint("______________________________________________________________________________")
    # pprint(id)
    #
    # questionData = Question.objects.all()
    # ansData = Answer.objects.all()
    # delete=Answer.objects.get(id=id)
    #
    # if delete:
    #
    #          try:
    #               delete.delete()
    #               return render(request, "Answer.html",
    #                            {"msg": "Answer  successfully submit.", "questionData": questionData, "ansData": ansData})
    #
    #          except Exception as e:
    #           return render(request, "Answer.html",{"msg": "Answer  successfully submit.", "questionData": questionData, "ansData": ansData})
    #
    #
    # else: return render(request, "Answer.html",{"msg": "Answer  successfully submit.", "questionData": questionData, "ansData": ansData})





@login_required(login_url="/login/")
def AnswerUpdate(request):
    return render(request, "base.html")


@login_required(login_url="/login/")
def Home(request):
    return render(request, "base.html")

def Index(request):
    return render (request,"index.html")

def ProfileList(request):
    profileData=Profile.objects.all()
    # projectData = Project.objects.all()

    return render (request,"memberList.html",{"profile":profileData})




def ProfileDetails(request,id):


    profileData = Profile.objects.get(pk=id)
    # pprint(profileData.companyName)
    projectData = Project.objects.filter(profile=profileData)

    # pprint(profileData.companyName)
    # data = Question.objects.get(pk=Answer.objects.get(ans.answerField))

    # pprint(profileData)
    # pprint(projectData)

    return render (request,"memberDetails.html",{'profile':profileData,'project':projectData})

def mailSend(request):
    email = EmailMessage('Hello', 'Django', to=['nkscoder@gmail.com'])
    email.send()
    return render (request,"index.html")
