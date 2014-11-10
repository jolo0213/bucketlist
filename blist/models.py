from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BL(models.Model):
	owner = models.ForeignKey(User)
	bl_name = models.CharField(max_length=50)

	def __str__(self):
		return self.bl_name

class Item(models.Model):
	bucket = models.ForeignKey(BL)
	item_value = models.CharField(max_length=200)
	def __str__(self):
		return self.item_value