from django.db import models
from django.contrib import admin


from Projects.models import Project
from CustomUser.models import User


class Thread(models.Model):
	project = models.ForeignKey(Project, unique=True)
	






class Message(models.Model):
	sender = models.ForeignKey(User, related_name='messages')
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	
	
	
	


class ThreadedMessage(Message):
	thread = models.ForeignKey(Thread)
	parent_object = models.ForeignKey('self', related_name = 'replies')
	is_reply = models.BooleanField(default=False)
	





class PersonalMessage(Message):
	recipient = models.ForeignKey(User) 
	



admin.site.register(PersonalMessage)

