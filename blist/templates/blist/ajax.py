from django.utils import simplejson

from dajaxice.decorators import dajaxice_register

from blist.models import Item

@dajaxice_register
def auto_filter_search_term(request, search_term):
	q = Item.objects.filter(item_value__istartswith=search_term)
	data = []
	for item in q:
		data_item = item.item_value + ' in ' + item.bucket
		data.append(data_item)
	return simplejson.dumps(data)