from django import template
from django.template.base import TemplateSyntaxError
from django.template import Node

register = template.Library()

@register.assignment_tag(takes_context=True)
def unread_notifications(context):
	if 'user' not in context:
		return ''

	user = context['user']
	if user.is_anonymous():
		return ''
	return user.notification_set.filter(status='UNREAD')