from django.contrib.gis.db import models
from django.contrib import admin

from Event.models import Event

class Marker(models.Model):
	geometry = models.PointField(srid=4326)
	event = models.ForeignKey(Event, unique=True, related_name = "marker", blank=True, null=True)
	objects = models.GeoManager()

	def __unicode__(self):
		return "(%s ,%s)" %(self.geometry.x, self.geometry.y)

admin.site.register(Marker)
