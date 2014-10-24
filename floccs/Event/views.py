import ujson as json

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core import serializers
from django.template import RequestContext
from django.contrib.gis.geos import Point

from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session


from Event.models import Event
from Event.forms import NewEventForm

from Markers.models import Marker

import redis

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)



class ShowEvents(View):
	def get(self, request, *args, **kwargs):
		events = serializers.serialize('json', Event.objects.all())
		return HttpResponse(events, content_type='application/json')
		# template_name = "events.html"
		# context  = {}
		# markers = Marker.objects.select_related('event').all()
		# return render_to_response(template_name, context, RequestContext(request))



class CreateNewEvent(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = {}
		form = NewEventForm()
		template_name = 'newEvent.html'

		context['eventForm'] = form
		return render_to_response(template_name, context, RequestContext(request))

	def post(self, request,  *args, **kwargs):
		form = NewEventForm(request.POST)
		if form.is_valid():
			#add logic to check for empty marker coordinates, coordinates overlap.
			if request.POST.get('data'):
				geo_data = json.loads(request.POST['data'])	
				new_marker = Marker()
				new_marker.geometry = Point(geo_data['geometry']['coordinates'][1],geo_data['geometry']['coordinates'][0])
				
				new_event = Event()
				new_event.name= form.cleaned_data['name']
				new_event.description = form.cleaned_data['description']
				new_event.image = request.FILES.get('image')
				#image type check
				#new_event.expiry_date = form.cleaned_data.get('expiry_date')
				new_event.creator = self.request.user
				

				try:
					new_event.save()
					new_marker.event = new_event
					new_marker.save()
					return HttpResponse('ok')
				except Exception, e:
					print e
					# output exceptions to user

			else:
				#output in json
				return HttpResponse('please place a marker on map')
		else:
			return HttpResponse(form.errors)




def event_room(request, event_id):
	try:
		event = Event.objects.get(id=event_id)
	except Exception,e:
		return HttpResponse(e)
	context = {}
	context['event'] = event

	return render_to_response("eventRoom.html", context, RequestContext(request))


class EventRoom(View):
	def get(self, request, *args, **kwargs):
		try:
			event = Event.objects.get(id=kwargs['event_id'])
		except Exception,e:
			return HttpResponse(e)
		context = {}
		context['event'] = event

		return render_to_response("eventRoom.html", context, RequestContext(request))


@login_required
def addFollower(request):
	if request.is_ajax:
		response_dict = {}
		event = Event.objects.get(id = request.POST.get('event_id'))
		try:
			event.addFollower(request.user)
			response_dict['status'] = u'success'
			return HttpResponse(json.dumps(response_dict), content_type="application/json")
		except Exception, e:
			print e
	else:
		event = Event.objects.get(id = request.POST.get('event_id'))
		event.addFollower(request.user)
		return HttpResponse('ok')

@login_required
def removeFollower(request):
	if request.is_ajax:
		response_dict = {}
		event = Event.objects.get(id = request.POST.get('event_id'))
		try:
			event.removeFollower(request.user)
			response_dict['status'] = u'success'
			return HttpResponse(json.dumps(response_dict), content_type="application/json")
		except Exception, e:
			print e
	else:
		event = Event.objects.get(id = request.POST.get('event_id'))
		event.removeFollower(request.user)
		return HttpResponse('ok')

def node_api(request):
	try:
		session = Session.objects.get(session_key=request.POST.get('sessionid'))
		user_id = session.get_decoded().get('_auth_user_id')
		user = User.objects.get(id=user_id)

		r = redis.StrictRedis(host='localhost', post=6379, db=0)
		r.publish('chat', user.username + ':' + request.POST.get('comment'))

		return HttpResponse('worked')

	except Exception, e:
		return HttpResponseServerError(str(e))
