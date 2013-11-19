from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

class Item(models.Model):

	STOLEN_OPTION = (
		('ns', 'Not Stolen'),
		('s', 'Stolen'),
		)

	device = models.CharField(max_length=250, 
		#help_text='Enter device name'
		)
	imei = models.CharField(max_length=15, unique=True, 
		#help_text='Add IMEI number'
		)
	description = models.TextField(
		#help_text='Describe your device'
		)

	stolen = models.CharField(max_length=2, choices=STOLEN_OPTION,)

	pub_date = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(User)


	def __unicode__(self):
		return self.device

	def get_absolute_url(self):
		#return reverse('views.search', args=[self.imei])
		return reverse('detail', kwargs={'item_imei': self.imei})