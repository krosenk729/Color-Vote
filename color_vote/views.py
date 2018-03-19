from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from random import randint

from .models import Word, Vote
from .forms import VoteForm

def home(request):
	return render(request, 'home.html', {'show_nav': False})

def results(request):
	# for each word
	# calc average green
	# calc average blue
	# calc average red
	# render list
	all_words = Word.objects.all()
	for word in all_words:
		word.red = word.green = word.blue = 0
		votes = Vote.objects.all().filter(word=word)
		l = len(votes)
		for vote in votes:
			word.red += int(vote.red(), 16) / l
			word.green += int(vote.green(), 16) / l
			word.blue += int(vote.blue(), 16) / l
	return render(request, 'results.html', {'words': all_words, 'show_nav': True})

def vote(request):
	# get random word and show in template
	# user_color = form value
	# on post, save color 
	# https://stackoverflow.com/questions/22392253/using-html5-input-type-color
	# https://github.com/wesleyllewis/PollsPythonDjangoTutorial/blob/master/polls/views.py
	randIndex = randint(0, len(Word.objects.all())-1)
	word = Word.objects.all()[randIndex]
	form = VoteForm()
	return render(request, 'vote.html', {'word': word, 'form': form, 'show_nav': True})

def vote_post(request, word):
	# receive post for word in url
	if request.method == 'POST':
		form = VoteForm(data = request.POST)
		if form.is_valid():
			vote = form.save(commit=False)
			vote.word = Word.objects.get(name=word)
			vote.save()
	return HttpResponseRedirect('/vote/success')

def vote_success(request):
	return render(request, 'success.html', {'show_nav': False})