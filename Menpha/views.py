from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render_to_response('contact.html')

def privacy(request):
	return render_to_response('privacy.html')

def team(request):
	return render_to_response('team.html')

def story(request):
	return render_to_response('story_behind.html')

def start(request):
	return render_to_response('get_started.html')

def faq(request):
	return render_to_response('faq.html')

def donate(request):
	return render_to_response('donate.html')

def technology(request):
	return render_to_response('technology.html')

def developer(request):
	return render_to_response('developer.html')


def file_not_found_404(request):
	return render(request, '404.html')

def server_error(request):
	return render(request, '500.html')

def perm_denied(request):
	return render(request, '403.html')