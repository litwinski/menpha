# Forms.py Handwritten by google.com/+Nkansahrexford
from django import forms
from django.forms import ModelForm
from main.models import Item
from django.utils.translation import ugettext as _


class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('device', 'slug', 'type_of_item', 'description', 'photo', 'stolen')
		labels = {
			'device': _('Name of the device'),
			'slug': _('Unique Identifier ( IMEI, Serial number, etc )'),
			'type_of_item': _('Select type of'),
			'stolen': _('Indicate state of device'),
			'photo': _('Photo of your device (optional)')
		}

class NotifyForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	#sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class ContactForm(forms.Form):
	#name = forms.CharField(max_length=100)
	subject = forms.CharField(max_length=300)
	sender = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)
	cc_myself = forms.BooleanField(required=False)

	#device = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Device name'}))
	#imei = forms.CharField(max_length=15, 
	#	widget=forms.TextInput(attrs={'placeholder':'IMEI '})
	#	)
	#description = forms.CharField(widget=forms.Textarea(
	#	attrs={'placeholder':'Describe device', 
	#			'cols':50,
	#			'rows':4,
	#			'max_length': 350,
	#	}))
