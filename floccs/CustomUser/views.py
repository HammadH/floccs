from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View
from CustomUser.models import User
from Projects.models import Project
from Profile.models import ProfileObject


class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class UserIdentificationMixin(object):                     #how to use mixin?
	def check_user(self, request, *args, **kwargs):
		user = User.objects.get(username=kwargs['username'])
		if user == self.request.user:
			return HttpResponse('other')


class NewProfileView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		template_name = 'new_profile.html'
		context = self.prepare_context(request)
		return render_to_response(template_name, context, RequestContext(request))

	def post(self, request, *args, **kwargs):
		if request.POST.has_key('title'):
			profile_object = ProfileObject.objects.create(user = request.user, title=request.POST.get('title'), info=request.POST.get('info'))
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	def prepare_context(self, request):
		context = {}
		context['profile_objects'] = request.user.profileobject_set.all()
		return context


class SelfProfileView(LoginRequiredMixin,  View):  
	def get(self, request, *args, **kwargs):
		if request.user == User.objects.get(username=kwargs['username']):
			template_name = 'profile.html'
			context = self.prepare_context(request)
			return render_to_response(template_name, context, RequestContext(request))
		else:
			return HttpResponseForbidden()
	def post(self, request, *args, **kwargs):
		if request.POST.has_key('title'):
			profile_object = ProfileObject.objects.create(user = request.user, title=request.POST.get('title'), info=request.POST.get('info'))
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	def prepare_context(self, request):
		context = {}
		context['profile_objects'] = request.user.profile_objects.all()
		return context

class OtherProfileView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		template_name = 'other_profile.html'
		context = {}
		context['member'] = User.objects.select_related('profile_objects').get(username=kwargs['username'])

		return render_to_response(template_name, context, RequestContext(request))

	





class HomeView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		template_name = 'home.html'
		context = self.prepare_context(request)
		return render_to_response(template_name, context, RequestContext(request))


	def prepare_context(self, request):
		context = {}
		context['projects'] = Project.objects.order_by('-created_on')

		return context


