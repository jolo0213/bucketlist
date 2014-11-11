from django.db import models
from django.conf import settings

# Create your models here.
class BL(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	bl_name = models.CharField(max_length=50)

	def __str__(self):
		return self.bl_name

class Item(models.Model):
	bucket = models.ForeignKey(BL)
	item_value = models.CharField(max_length=200)
	item_url = models.URLField(max_length=200,null=True)
	item_desc = models.CharField(max_length=1000,null=True)
	def __str__(self):
		return self.item_value
		