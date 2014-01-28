from django.conf.urls import patterns, include, url

from Message.views import InboxView,conv

urlpatterns = patterns('',

    url(r'^', InboxView.as_view(), name='inbox'),
    url(r'^(?P<other_person>\w+)/', conv, name='conversation'),
    
)
