from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

def help(request):
	return render(request, 'help.html')

def faq(request):
	return render_to_response('faq.html')

def privacy(request):
	return render_to_response('help.html')