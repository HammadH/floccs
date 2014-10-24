import os

from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

from Message.models import Message
from CustomUser.models import User

from sorl.thumbnail import ImageField

def event_image_path(instance, filename):
	
	return os.path.join(
		"media/event_images", "%s" %instance, filename)


class Event(models.Model):
	name = models.CharField(max_length=100, blank=False) 
	description = models.TextField()
	image = ImageField(upload_to=event_image_path, blank=True, null=True)
	
	messages = models.ManyToManyField(Message, related_name="event", blank=True)
	#chatroom = models.ForeignKey(Chatroom, unique=True, related_name="event")
	creator = models.ForeignKey(User,  related_name="event")
	expiry_date = models.DateTimeField(blank=False, auto_now_add=True)  #auto now add must be removed.
	#is_expired = models.BooleanField(default=False)
	#location = models.ForeignKey(Location, unique=True, related_name="event")
	followers = models.ManyToManyField(User, related_name='events', blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	def set_expiry_limit():
		pass

	def expire_event(self):
		pass


	def addFollower(self, user):
		if user and user not in self.followers.all():
			self.followers.add(user)
			#update user's following events.
			return True
		else:
			return False

	def removeFollower(self, user):
		if user in self.followers.all():
			self.followers.remove(user)
			return True
		else:
			return False

	def get_absolute_url(self):
		return reverse('event_room', kwargs={'event_id':self.id})

admin.site.register(Event)