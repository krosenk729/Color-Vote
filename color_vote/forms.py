from django import forms
from .models import Vote
from django.contrib.admin import widgets
from django.forms.widgets import TextInput
# from django.forms import ModelForm

class VoteForm(forms.ModelForm):
	class Meta:
		model = Vote
		fields = ['color']
		widgets = {'color': TextInput(attrs={'type': 'color', 'value': '#7d7d7d'})}