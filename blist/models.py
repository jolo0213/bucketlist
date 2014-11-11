from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_full(value):
    	if value is None:
       		raise ValidationError('You cannot leave Item Name blank!')

# Create your models here.
class BL(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	bl_name = models.CharField(max_length=50)
	favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.bl_name

class Item(models.Model):
	bucket = models.ForeignKey(BL)
	item_value = models.CharField(max_length=200,validators=[validate_full])
	item_url = models.URLField(max_length=200,null=True,blank=True)
	item_desc = models.CharField(max_length=1000,null=True,blank=True)
	finish = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.item_value
