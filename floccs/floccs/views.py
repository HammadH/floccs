from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic import View
from django.contrib.auth import logout

from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from CustomUser.forms import UserForm
from CustomUser.models import User






class IndexView(View):
	def get(self, request, *args, **kwargs):
		template_name = 'landing_page.html'
		context = self.prepare_context(request)
		return render_to_response(template_name, context, RequestContext(request))

	def post(self, request, *args, **kwargs):
		if request.POST.has_key('login_form'):
			try:
				user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
			
				if user is not None:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect(reverse('home')) 
					else:
						return HttpResponse('You need to activate your account from email ')
				else:
					return HttpResponse('user is none')
			except:
				return HttpResponse('invalid login')

		elif request.POST.has_key('signup_form'):
			form = UserForm(request.POST)
			if form.is_valid:
				new_user = form.save()
				return HttpResponseRedirect(reverse('new_profile', kwargs={'username':new_user.username}))
				
					
			else:
				return HttpResponse("invalid data entered")


		

	def prepare_context(self, request):
		context = {}
		context['login_form'] = AuthenticationForm()
		context['signup_form'] = UserForm()
		return context



def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
