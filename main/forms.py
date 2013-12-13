# Forms.py Handwritten by google.com/+Nkansahrexford
from django import forms
from django.forms import ModelForm
from main.models import Item
from django.utils.translation import ugettext as _


class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('device', 'slug', 'description', 'photo', 'stolen')
		labels = {
			'device': _('Name of my device'),
			'slug': _('IMEI of my device'),
			'stolen': _('Indicate state of device'),
			'photo': _('Photo of your device (optional)')
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
