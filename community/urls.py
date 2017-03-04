"""community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views import *
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # url(r'^core/', include('core.urls')),
    url(r'^$', Index),
    url(r'^admin/', admin.site.urls),
    url(r"^register/", CreateUser),
    url(r"^login/",login),
    url(r"^dashboard/",dashboard),
    url(r"^update/",update),
    url(r"^project/",project),
    url(r"^question/",QuestionView),
    url(r"^answer/",AnswerView),
    url(r'^answerupdate/(?P<id>[0-9]+)/$', AnswerUpdate, name='answerupdate'),
    url(r'^answerdelete/(?P<id>[0-9]+)/', AnswerDelete, name='answerdelete'),
    url(r"^home/",Home),
    url(r"^signup/",Signup),
    # url(r"^singleprofile/", SingleProfile),
    url(r"^menberlist/", ProfileList),
    url(r'^profiledetails/(?P<id>[0-9]+)/', ProfileDetails),
    url(r"^mailSend/", mailSend),




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)