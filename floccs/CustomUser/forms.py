from django import forms




from CustomUser.models import User

class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'place_of_stay']
		widgets = {
			'password': forms.PasswordInput(),
		}

	def save(self, commit=True, force_insert=False, force_update=False, *args, **kwargs):
		new_user = super(UserForm, self).save(commit=False, *args, **kwargs)
		new_user.set_password(self.cleaned_data['password'])
		if commit:
			new_user.save()
		return new_user


