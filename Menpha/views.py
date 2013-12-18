from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def privacy(request):
	return render(request, 'privacy.html')

def team(request):
	return render(request, 'team.html')

def story(request):
	return render(request, 'story_behind.html')

def start(request):
	return render(request, 'get_started.html')

def faq(request):
	return render(request, 'faq.html')

def donate(request):
	return render(request, 'donate.html')

def technology(request):
	return render(request, 'technology.html')

def developer(request):
	return render(request, 'developer.html')


def file_not_found_404(request):
	return render(request, '404.html')

def server_error(request):
	return render(request, '500.html')

def perm_denied(request):
	return render(request, '403.html')