from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from Message.models import PersonalMessage, Conversation

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class InboxView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = {}
		context['conversations'] = request.user.conversations.all()
		return render_to_response('inbox.html',context,  RequestContext(request))



class ConversationView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		
		return HttpResponse('ok')

		context = {}
		context['messages'] = Conversation.objects.get(user = request.user, other_person=kwargs['other_person']).messages.all()
		return render_to_response('conversation.html', context,  RequestContext(request))



def conv(request, other_person):
	return HttpResponse('ok')