from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail
from main.forms import ContactForm

def about(request):
	return render(request, 'about.html')

def contact(request):
	""" Send contact emails """
	if request.method == "POST": # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
		# Process the data in form.cleaned_data
			#name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['seanmavley@gmail.com']

			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/app/email/thanks/') # Redirect after POST
	else:
		form = ContactForm() # An unbound form
	return render(request, 'contact.html', {'form': form,})

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