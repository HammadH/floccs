from django.shortcuts import render_to_response
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView


from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from Projects.models import Project
from Projects.forms import ProjectForm
from CustomUser.models import User
from Message.models import ProjectMessage



class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class NewProjectView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = {}
		form = ProjectForm(initial={'owner':self.request.user})

		template_name='new_project.html'

		context['form'] = form
		return render_to_response(template_name, context, RequestContext(request))
	
	def post(self, request, *args, **kwargs):
		form = ProjectForm(request.POST)
		if form.is_valid():
			new_project = Project()
			new_project.name = form.cleaned_data['name']
			new_project.description = form.cleaned_data['description']
			new_project.owner = self.request.user
			new_project.save()
			for tag in form.cleaned_data['tags']:
				new_project.tags.add(tag)
			return HttpResponseRedirect(reverse('home'))

		else:
			return HttpResponse('Invalid form! Please fill correctly')

class ProjectDetailView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		context = {}
		context['project'] = Project.objects.prefetch_related('followers').prefetch_related('messages__sender').select_related('owner').get(id=kwargs['id'])
		return render_to_response('project_detail.html', context, RequestContext(request))


	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			pass




		else:
			 new_message = ProjectMessage()
			 new_message.sender = request.user
			 new_message.message = request.POST.get('message')
			 new_message.project = Project.objects.get(id = int(request.POST.get('project')))
			 new_message.is_reply = request.POST.get('is_reply')
			 if request.POST['is_reply'] == 'False':
			 	new_message.parent_object = None
			 elif request.POST['is_reply'] == 'True':
			 	new_message.parent_object=ProjectMessage.objects.get(id=int(request.POST['parent']))
			 try:
			 	new_message.save()
			 except:
			 	return HttpResponse('something went wrong')
			 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			 

			 




class UserProjectsListView(LoginRequiredMixin, ListView):
	model = Project
	template_name = 'my_projects.html'
	
	def get_queryset(self):
		return Project.objects.filter(owner=self.request.user)


class ProjectEditView(LoginRequiredMixin, UpdateView):
		
		

		def get(self, request, *args, **kwargs):
			template_name = 'edit_project.html'
			project = Project.objects.get(id = kwargs['id'])
			
			form = ProjectForm({'name':project.name, 'description':project.description, 'tags':", ".join(map(str,[tag.name for tag in project.tags.all()]))})
			return render_to_response(template_name,{'form':form, 'id':project.id}, RequestContext(request))


		def post(self, request, *args, **kwargs):
			form = ProjectForm(request.POST, instance = Project.objects.get(id=request.POST['project_id']))
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			else:
				return HttpResponse('Invalid form')


def addFollower(request, project_id):
	if request.method == "GET":
		if request.is_ajax():
			pass

		else:
			
			project = Project.objects.get(id = project_id)
			if request.user == project.owner:
				return HttpResponse('It is your project!')
			else:	
				project.add_follower(request.user)
				return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
	


	else:
		return HttpResponseForbidden()


def removeFollower(request, project_id):
	pass



