from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

def validate_full(value):
	if value is None:
		raise ValidationError('You cannot leave Item Name blank!')

# Create your models here.
class BL(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=50)
	favorite = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('blist:items', args=[self.id,])

	def get_share_url(self):
		return 'http://' + str(Site.objects.get(id=1)) + str(self.get_absolute_url()) + 'share'

	def __unicode__(self):
		return self.name

class Item(models.Model):
	bucket = models.ForeignKey(BL)
	item_value = models.CharField(max_length=200, validators=[validate_full])
	item_url = models.URLField(max_length=200,null=True,blank=True)
	item_desc = models.CharField(max_length=500,null=True,blank=True)
	finish = models.DateField(null=True,blank=True)

	def __unicode__(self):
		return self.item_value