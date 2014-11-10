from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from blist.models import BL, Item
from blist.forms import ItemForm, BLForm

# Create your views here.
@login_required
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

@login_required
def items(request, bucket_id):
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
	return render(request,'blist/items.html',{'bucket':bucket,'form':add_form})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/blist/")
	else:
		form = UserCreationForm()
	return render(request, "blist/register.html", {'form': form,})

@login_required
def delete_item(request, item_id):
	item = get_object_or_404(Item,pk=item_id)
	bucket = item.bucket
	item.delete()
	return HttpResponseRedirect(reverse('blist:items', args=[bucket.pk]))

@login_required
def delete_bucket(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id)
	bucket.delete()
	return HttpResponseRedirect('/blist/')