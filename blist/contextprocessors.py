import json

from blist.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def autocomplete(request):
	source = Item.objects.filter(bucket__owner=request.user).values('item_value')
	ivals = []
	for item in source:
		ivals.append(item['item_value'])
	ivals = json.dumps(ivals)
	# ivals = json.dumps(list(Item.objects.filter(bucket__owner=request.user).values_list('item_value',flat=True)))
	return { 'source':ivals }
	