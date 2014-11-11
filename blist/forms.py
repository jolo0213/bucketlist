from django.forms import ModelForm, ModelChoiceField
from django import forms

from blist.models import BL, Item

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('item_value','item_url','item_desc')

class BLForm(ModelForm):
	class Meta:
		model = BL
		fields = ('bl_name',)