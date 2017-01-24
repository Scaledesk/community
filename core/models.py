from __future__ import unicode_literals



from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (("M","Male"),("F","Female"))
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES, default="M")

class UserDipp(models.Model):
      email = models.EmailField(max_length=256, unique=True)
      dipp = models.IntegerField()
      status=models.IntegerField(default=0)
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
      def __unicode__(self):
            return self.companyName

