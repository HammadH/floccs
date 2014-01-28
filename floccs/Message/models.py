from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse


from Projects.models import Project
from CustomUser.models import User






class Message(models.Model):
	sender = models.ForeignKey(User, related_name='messages')
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	
	



	
class ProjectMessage(Message):
	project = models.ForeignKey(Project, related_name='messages')
	parent_object = models.ForeignKey('self', related_name = 'replies', null=True)
	is_reply = models.BooleanField(default=False)
	














class PersonalMessageManager(models.Manager):
	def create_with_conversation(self, sender, recipient, message):
		new_message = PersonalMessage()
		new_message.sender = sender
		new_message.recipient = recipient
		new_message.message = message
		try:
			new_message.save()
		except:
			return None
		c, created = Conversation.objects.get_or_create(other_person=new_message.sender, user=recipient)
		c.messages.add(new_message)
		return new_message




class PersonalMessage(Message):
	recipient = models.ForeignKey(User) 

	objects_ = PersonalMessageManager()
	

	def __unicode__(self):
		return self.message
	

class Conversation(models.Model):
	user = models.ForeignKey(User, related_name='conversations')
	other_person = models.ForeignKey(User, related_name='conv')  #where is this related_name used?
	messages = models.ManyToManyField(PersonalMessage, null=True)

	def __unicode__(self):
		return "Conversation with %s" %self.other_person

	def get_absolute_url(self):
		return reverse('conversation', kwargs={'other_person':self.other_person})


admin.site.register(PersonalMessage)
admin.site.register(Conversation)

