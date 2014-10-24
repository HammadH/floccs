from django.conf.urls import patterns, include, url
from Event.views import CreateNewEvent, ShowEvents, EventRoom, addFollower, removeFollower,event_room, node_api
import socketio.sdjango

urlpatterns = patterns('',
    
    url(r'^$', ShowEvents.as_view(), name='show_events'),
    url("^socket\.io", include(socketio.sdjango.urls)),
 #  url(r'^event_room/(?P<event_id>[\d]+)/', EventRoom.as_view(), name='event_room'),
 	url(r'^event_room/(?P<event_id>[\d]+)/', event_room, name='event_room'),
    url(r'^create/', CreateNewEvent.as_view(), name='create_event'),
   #url(r'^edit/', CreateNewEvent.as_view(), name='create_event'),
   # url(r'^delete/', CreateNewEvent.as_view(), name='create_event'),
   	url(r'^add_follower/', addFollower, name='add_follower'),
   	url(r'^remove_follower/', removeFollower, name='remove_follower'),
   	url(r'^node_api/', node_api, name='node_api'),


    
)
