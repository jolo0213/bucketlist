from django.forms import ModelForm, Textarea
from django import forms

from blist.models import BL, Item, SharedList

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('item_value','item_url','item_desc')
		widgets = {'item_desc': Textarea(attrs={'cols': 35, 'rows': 7}),}

class BLForm(ModelForm):
	class Meta:
		model = BL
		fields = ('name',)

class SharedForm(ModelForm):
	class Meta:
		model = SharedList
		fields = ('name',)
		