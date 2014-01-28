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



class Project(models.Model): 
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	followers = models.ManyToManyField(User, related_name='following_projects', blank=True, null=True)
	project_status = models.CharField(max_length=10, choices = PROJECT_STATUS, default='OPEN')
	project_workers = models.ManyToManyField(User, related_name='working_on_projects', null=True, blank=True)
	tags = TaggableManager()

	#chatroom = models.ForeignKey(ChatRoom, unique=True)

	def __unicode__(self):
		return "%s" %self.name

	def get_absolute_url(self):
		return reverse('project_details', kwargs={'id':self.id })

	def edit_project_url(self):
		return reverse('edit_project', kwargs={'id':self.id})

	def add_follower(self, user): #add a follower and send a message to the user
		self.followers.add(user)

	def remove_follower(self, user):
		self.followers.remove(user)

	def request_to_work(self, user):
		pass

	def show_work_requests(self):
		return self.work_requests.all() 

	def show_accepted_work_requests(self):
		return self.work_requests.filter(is_sender_accepted=True)

	def process_work_request(self, request):
		if request.is_sender_accepted==True:
			self.add_worker_to_project(request.sender)
			#notify worker that he has been accepted
			return True
		else:
			return False

	def add_worker_to_project(self, user):
		if user not in self.project_workers:
			self.project_workers.add(user)
			return True
		else:
			return False


class ProjectUpdate(models.Model):
	project = models.ManyToManyField(Project, related_name='updates')
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.message

class WorkRequest(models.Model):
	""" Object that is used for notifying the user that someone is interested \
	work on his/her project. It is like a friend request and determines whether\
	the person is allowed to work or no"""
	project = models.ManyToManyField(Project, related_name='work_requests')
	sender = models.ForeignKey(User, related_name='my_work_requests')
	recipient = models.ForeignKey(User, related_name='recieved_work_requests')
	timestamp = models.DateTimeField(auto_now_add=True)
	is_sender_accepted = models.BooleanField(default=False)


	def __unicode__(self):
		return "%s would like to work on %s" %(sender, project)





	# send post_save for notifications to connect






admin.site.register(Project)

