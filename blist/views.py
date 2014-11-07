from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from blist.models import BL, Item
from blist.forms import ItemForm, BLForm

# Create your views here.
def index(request):
	bucket_list = BL.objects.all()
	if request.method == 'POST':
		add_list_form = BLForm(request.POST)
		if add_list_form.is_valid():
			bucket_list = add_list_form.save()
			return HttpResponseRedirect(reverse('blist:items', args=[bucket_list.pk]))
	else:
		add_list_form = BLForm()
	return render(request,'blist/index.html',{'bucket_list':bucket_list,'form':add_list_form})

def items(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id)
	return render(request,'blist/items.html',{'bucket':bucket})

def add(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id) 
	if request.method == 'POST':
		add_form = ItemForm(request.POST)
		if add_form.is_valid():
			bucket_item = add_form.save(commit=False)
			bucket_item.bucket = bucket
			bucket_item.save()
			return HttpResponseRedirect(reverse('blist:items', args=[bucket.pk]))
	else:
		add_form = ItemForm()
	return render(request, 'blist/add_item.html',{'bucket':bucket, 'form': add_form})