from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View

from Profile.models import ProfileObject


class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)



class ProfileView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		template_name = 'profile.html'
		return render_to_response(template_name, RequestContext(request))

	def post(self, request, *args, **kwargs):
		pass

