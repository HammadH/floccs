from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from CustomUser.models import User

from taggit.managers import TaggableManager



PROJECT_STATUS = (
	('OPEN' , 1),
	('CLOSED', 0),
)

class Project(models.Model): #ideas or projects
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	followers = models.ManyToManyField(User, related_name='following_ideas', blank=True, null=True)
	project_status = models.CharField(max_length=10, choices = PROJECT_STATUS, default='OPEN')

	tags = TaggableManager()

	#chatroom = models.ForeignKey(ChatRoom, unique=True)

	def __unicode__(self):
		return "%s" %self.name

	def get_absolute_url(self):
		return reverse('project_details', kwargs={'id':self.id })

	def add_follower(self, user): #add a follower and send a message to the user
		self.followers.add(user)



	def remove_follower(self, user):
		self.followers.remove(user)





admin.site.register(Project)

