import json

from blist.models import Item

def autocomplete(request):
	if request.user.is_authenticated():
		ivals = json.dumps(list(Item.objects.filter(bucket__owner=request.user).values_list('item_value',flat=True)))
		return { 'source':ivals }
	else:
		return { 'source':[] }