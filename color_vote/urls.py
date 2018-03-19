from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('vote', views.vote, name='vote'),
	path('vote/<slug:word>', views.vote_post, name='vote_post'),
	path('vote/success', views.vote_success, name='vote_success'),
	path('results', views.results, name='results'),
]