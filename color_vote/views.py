from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
	return True

def results(request):
	# for each word
	# calc average green
	# calc average blue
	# calc average red
	# render list
	return True
	

def vote(request):
	# get random word and show in template
	# user_color = form value
	# on post, save color 
	# https://github.com/wesleyllewis/PollsPythonDjangoTutorial/blob/master/polls/views.py
	return HttpResponse()