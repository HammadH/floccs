from django import forms

from Event.models import Event

from bootstrap3_datetime.widgets import DateTimePicker


class NewEventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'description', 'image',]
		# widgets = {
		# 	'expiry_date': DateTimePicker(options={"format":"YYYY-MM-DD HH:mm",
		# 											"pickSeconds": False
		# 											})
			
		# }
		