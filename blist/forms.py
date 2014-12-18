from django.forms import ModelForm, Textarea
from django import forms

from blist.models import BL, Item, SharedList

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('item_value','item_url','item_desc')
		widgets = {
			'item_value':forms.TextInput(attrs={
				'placeholder':'Item Name',
				'class':'form-control',
				}),
			'item_desc': Textarea(attrs={
				'placeholder':'Description (optional)',
				'class':'form-control',
				}),
			'item_url':forms.TextInput(attrs={
				'placeholder':'URL (optional)',
				'class':'form-control',
				}),
			}

class BLForm(ModelForm):
	class Meta:
		model = BL
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs={
				'placeholder':'List Name','class':'form-control'
				}),
			}

class SharedForm(ModelForm):
	class Meta:
		model = SharedList
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs={
				'placeholder':'Username','class':'form-control'
				}),
			}