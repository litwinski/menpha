# Models.py Handwritten by google.com/+Nkansahrexford
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Item(models.Model):
	""" Main model for the Menpha app. """

	TYPE_OF_ITEM = (
		('auto', 'Automobile'),
		('md', 'Mobile Devices'),
		('com', 'Computers'),
		('da', 'Domestic Appliance'),
	)

	STOLEN_OPTION = (
		('ns', 'Its with me'),
		('s', 'Its stolen/missing'),
	)

	device = models.CharField(max_length=250,)
	slug = models.SlugField(max_length=30, unique=True,)
	type_of_item = models.CharField(max_length=20, choices=TYPE_OF_ITEM)
	description = models.TextField()
	stolen = models.CharField(max_length=2, choices=STOLEN_OPTION)
	#photo = models.ImageField(upload_to='devices/', blank=True, null=True)
	photo = ProcessedImageField(blank=True, null=True, upload_to='devices/', processors=[ResizeToFill(250, 250)], format='JPEG', options={'quality': 80})
	pub_date = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User)

	def __unicode__(self):
		""" Returns device name """
		return self.device

	def get_absolute_url(self):
		""" For reverse url matching in views """
		#return reverse('views.search', args=[self.imei])
		return reverse('detail', kwargs={'slug': self.slug})