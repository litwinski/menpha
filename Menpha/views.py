from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render_to_response('contact.html')

def privacy(request):
	return render_to_response('privacy.html')


def file_not_found_404(request):
	return render(request, '404.html')

