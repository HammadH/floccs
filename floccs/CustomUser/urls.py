from django.conf.urls import patterns, include, url

from CustomUser.views import *


urlpatterns = patterns('',
    # Examples:
   # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<user>\w+)/profile/$', ProfileView.as_view(), name='profile'),


   
)
