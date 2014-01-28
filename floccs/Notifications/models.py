from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save
from django.contrib import admin

from CustomUser.models import User
from Message.models import PersonalMessage



NOTIFICATION_STATUS= (
	('UNREAD', 1),
	('READ', 0),
	)



NOTIFICATION_MESSAGES = (
	('New message '), 
	)


class Notification(models.Model):
	message = models.CharField(max_length = 150, blank=False, null=False)
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, choices = NOTIFICATION_STATUS, default='UNREAD')
	content_type = models.ForeignKey(ContentType, related_name='notifications', null=True)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey()

	
	def __unicode__(self):
		return "%s" %self.message

	def mark_read(self):
		self.status = 'READ'




admin.site.register(Notification)


def create_notifictions_handler(sender, instance, created,  **kwargs):
	if created:
		new_notif = Notification.objects.create(message = NOTIFICATION_MESSAGES[0], \
					user = instance.recipient, content_object=instance )



post_save.connect(create_notifictions_handler, sender=PersonalMessage , dispatch_uid='PersonalMessage_created')