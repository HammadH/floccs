from django import forms
from Projects.models import Project

class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ['name', 'description', 'tags']


