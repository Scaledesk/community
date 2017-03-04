from __future__ import unicode_literals



from django.db import models
from django.contrib.auth.models import User


class UserDipp(models.Model):
      email = models.EmailField(max_length=256, unique=True)
      dipp = models.IntegerField( unique=True)
      status=models.IntegerField(default=0)
      user=models.ForeignKey(User,null=True,blank=True)
      def __unicode__(self):
            return self.email
class Profile(models.Model):
      userdipp = models.OneToOneField(UserDipp)
      companyName=models.CharField(max_length=100)
      designatePerson=models.CharField(max_length=50)
      founderCofounder=models.CharField(max_length=50)
      website=models.CharField(max_length=50)
      mobile=models.IntegerField()
      address=models.CharField(max_length=256)
      city=models.CharField(max_length=25)
      state=models.CharField(max_length=30)
      pincode=models.IntegerField()
      facebook=models.CharField(max_length=256)
      linkedin=models.CharField(max_length=256)
      twitter = models.CharField(max_length=256)
      industry=models.CharField(max_length=100)
      provideSupport=models.CharField(max_length=500,default=0)
      needSupport=models.CharField(max_length=500, default=0)
      PROFILE_TYPE = (("Startup Companies", "Startup Companies"), ("Mentors/Consultants", "Mentors/Consultants"),
                      ("Investors(Angels/VC Funds)", "Investors(Angels/VC Funds)"), ("Accelerators", "Accelerators")
                      , ("Incubators", "Incubators"), ("Event Manager", "Event Manager"))
      profileType = models.CharField(max_length=100,choices=PROFILE_TYPE)

      def __unicode__(self):
            return self.companyName

class Project(models.Model):
      # userdipp = models.OneToOneField(UserDipp)
      profile = models.ForeignKey(Profile)
      companyName = models.CharField(max_length=100)
      brandName = models.CharField(max_length=100)
      BUSINESS_TYPE = (("B2B", "B2B"), ("B2C", "B2C"), ("C2B", "C2B"), ("B2B2C", "B2B2C"))
      typeOfBusiness = models.CharField(max_length=6, choices=BUSINESS_TYPE)
      url = models.CharField(max_length=100)
      description = models.CharField(max_length=300)
      logo = models.ImageField(upload_to='documents/')
      videoLink = models.CharField(max_length=256)
      aboutProductCompany = models.FileField(upload_to='documents/')
      investor =models.ImageField(upload_to='documents/')

class Question(models.Model):
      profile = models.ForeignKey(Profile)
      question=models.CharField(max_length=1000)
      def __unicode__(self):
            return self.question
class Answer(models.Model):
      question=models.ForeignKey(Question)
      answerField=models.CharField(max_length=1000)

      def __unicode__(self):
            return self.question.question