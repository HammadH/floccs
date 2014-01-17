from django.conf.urls import patterns, include, url

from Projects.views import *


urlpatterns = patterns('',
    # Examples:
   # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new/$', NewProjectView.as_view(), name='new_project'),
    url(r'^(?P<id>\d+)/$', ProjectDetailView.as_view(), name='project_details'),
    url(r'^my_projects/', UserProjectsListView.as_view(), name = 'my_projects'),
    url(r'^(?P<project_id>\d+)/follow_project/$', addFollower, name='add_follower'),
    url(r'^(?P<id>\d+)/unfollow_project/$', removeFollower, name='remove_follower'),
   


   
)
