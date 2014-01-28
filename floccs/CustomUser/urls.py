from django.conf.urls import patterns, include, url

from CustomUser.views import *

import socketio.sdjango


urlpatterns = patterns('',
    # Examples:
   # url(r'^$', HomeView.as_view(), name='home'),
    url('^socket\.io', include(socketio.sdjango.urls)),
    url(r'^new_profile/(?P<username>[\w.]+)$', NewProfileView.as_view(), name='new_profile'),
    url(r'^profile/(?P<username>[\w@.]*)$', SelfProfileView.as_view(), name='profile'),
    url(r'^view_profile/(?P<username>[\w.]*)$', OtherProfileView.as_view(), name='view_profile'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^project/', include('Projects.urls')),

    

   
)
