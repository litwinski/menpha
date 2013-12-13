# Models.py Handwritten by google.com/+Nkansahrexford
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Item(models.Model):

	TYPE_OF_ITEM = (
		('auto', 'Automobile'),
		('md', 'Mobile Devices'),
		('com', 'Computers'),
		)

	STOLEN_OPTION = (
		('ns', 'Its with me'),
		('s', 'Its stolen/missing'),
		)

	device = models.CharField(max_length=250, 
		#help_text='Enter device name'
		)
	slug = models.SlugField(max_length=15, unique=True, 
		#help_text='Add IMEI number'
		)
	type_of_item = models.CharField(max_length=5, choices=TYPE_OF_ITEM,)
	
	description = models.TextField(
		#help_text='Describe your device'
		)

	stolen = models.CharField(max_length=2, choices=STOLEN_OPTION,)

	#photo = models.ImageField(upload_to='devices/', blank=True, null=True)
	
	photo = ProcessedImageField(blank=True, null=True, upload_to='devices/', processors=[ResizeToFill(250, 250)], format='JPEG', options={'quality': 80})

	pub_date = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(User)


	def __unicode__(self):
		return self.device

	def get_absolute_url(self):
		#return reverse('views.search', args=[self.imei])
		return reverse('detail', kwargs={'slug': self.slug})

	#def photo_url(self):
	#	if self.photo and hasattr(self.photo, 'url'):
	#		self.photo.url
