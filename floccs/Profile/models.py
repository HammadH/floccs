from django.db import models

from CustomUser.models import User

class ProfileObject(models.Model):
	user = models.ForeignKey(User, related_name='profile_objects')
	title = models.CharField(max_length=150, blank=False)
	info = models.TextField(blank=True)


