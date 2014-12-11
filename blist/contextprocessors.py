import json

from blist.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def autocomplete(request):
	ivals = json.dumps(list(Item.objects.filter(bucket__owner=request.user).values_list('item_value',flat=True)))
	return { 'source':ivals }
	