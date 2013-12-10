# Forms.py Handwritten by google.com/+Nkansahrexford
from django import forms
from django.forms import ModelForm
from main.models import Item


class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('device', 'slug', 'description', 'photo', 'stolen')
		labels = {
			'device': 'Name of my device',
			'slug': 'IMEI of my device'
		}
		
	#device = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Device name'}))
	#imei = forms.CharField(max_length=15, 
	#	widget=forms.TextInput(attrs={'placeholder':'IMEI '})
	#	)
	#description = forms.CharField(widget=forms.Textarea(
	#	attrs={'placeholder':'Describe device', 
	#			'cols':50,
	#			'rows':4,
	#			'maxlength': 350,
	#	}))

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }﻿