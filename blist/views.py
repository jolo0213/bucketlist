import json

from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from blist.models import BL, Item, SharedList
from blist.forms import ItemForm, BLForm, SharedForm

# Create your views here.
@login_required
def index(request, faves=False):
	if faves == False:
		bucket_list = BL.objects.filter(owner=request.user)
	else:
		bucket_list = BL.objects.filter(owner=request.user,favorite=True)
	if request.method == 'POST':
		if request.is_ajax():
			add_list_form = BLForm(request.POST)
			if add_list_form.is_valid():
				bucket_list = add_list_form.save(commit=False)
				bucket_list.owner = request.user
				bucket_list.save()
				return HttpResponse(render_to_string('blist/lists.html', {'bucket':bucket_list}))
			else:
				return HttpResponse(status=400)
		else:
			return HttpResponse(status=403)
	else:
		add_list_form = BLForm()
	return render(request,'blist/index.html', {'bucket_list':bucket_list,'form':add_list_form,})

@login_required
def items(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id,owner=request.user)
	editors = SharedList.objects.filter(bucket=bucket.id).values_list('name',flat=True)
	users = User.objects.all().values_list('username',flat=True)
	if request.method == 'POST':
		if request.is_ajax():
			add_form = ItemForm(request.POST)
			if add_form.is_valid():
				bucket_item = add_form.save(commit=False)
				bucket_item.bucket = bucket
				bucket_item.save()
				return HttpResponse(render_to_string('blist/item_table.html', {'item':bucket_item,'bucket':bucket}))
			else:
				return HttpResponse(status=400)
	else:
		add_form = ItemForm()
		shared_form = SharedForm()
	return render(request,'blist/items.html', {
		'bucket':bucket,
		'form':add_form,
		'shared':shared_form,
		'editors':editors,
		'existing':json.dumps(list(editors)),
		'users':json.dumps(list(users)),})

@login_required
def add_editor(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id,owner=request.user)
	if request.method == 'POST':
		form = SharedForm(request.POST)
		if request.is_ajax():
			if form.is_valid():
				editor = form.save(commit=False)
				editor.bucket = bucket
				editor.save()
				return HttpResponse(status=200)
			else:
				return HttpResponse(status=400)
	return HttpResponse(status=200)

@login_required
def details(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id,bucket__owner=request.user)
	return render(request,'blist/details.html', {'item':item,})

@login_required
def delete_item(request, bucket_id, item_id):
	if request.is_ajax():
		item = get_object_or_404(Item,pk=item_id)
		item.delete()
		return HttpResponse(status=200)
	return HttpResponse(status=403)

@login_required
def delete_bucket(request, bucket_id):
	if request.is_ajax():
		bucket = get_object_or_404(BL,pk=bucket_id,owner=request.user)
		bucket.delete()
		return HttpResponse(status=200)
	return HttpResponse(status=403)

@login_required
def mod_favorite(request, bucket_id):
	if request.is_ajax():
		bucket = get_object_or_404(BL,pk=bucket_id,owner=request.user)
		bucket.favorite = not bucket.favorite
		bucket.save()
		return HttpResponse(status=200)
	return HttpResponse(status=403)

@login_required
def finish(request, bucket_id, item_id):
	if request.is_ajax():
		item = get_object_or_404(Item,pk=item_id)
		if item.finish != None:
			item.finish = None
		else:
			item.finish = datetime.now()
		item.save()
		return HttpResponse(status=200)
	return HttpResponse(status=403)

@login_required
def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			item = Item.objects.filter(item_value__icontains=q,bucket__owner=request.user)
			return render(request, 'blist/search.html', {'items':item,'query':q})
	return render(request, 'blist/search.html', {'error':error})

# Shared Views

@login_required
def shared_index(request):
	shared = SharedList.objects.filter(name=request.user).values_list('bucket_id',flat=True)
	bls = []
	for bl in shared:
		current = BL.objects.filter(pk=bl)
		bls.append(current[0])
	return render(request,'blist/shared_index.html',{'lists':bls if len(bls) else None})

@login_required
def shared_list(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id)
	if request.method == 'POST':
		if request.is_ajax():
			form = ItemForm(request.POST)
			if form.is_valid():
				bucket_item = form.save(commit=False)
				bucket_item.bucket = bucket
				bucket_item.save()
				return HttpResponse(render_to_string('blist/shared_items_table.html', {'item':bucket_item,'bucket':bucket}))
			else:
				return HttpResponse(status=400)
	else:
		form = ItemForm()
	return render(request,'blist/shared_items.html',{'bucket':bucket,'form':form})

@login_required
def shared_detail(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	return render(request,'blist/shared_detail.html', {'item':item,})

# Anonymous Views

def share(request, bucket_id):
	bucket = get_object_or_404(BL,pk=bucket_id)
	return render(request,'blist/share.html', {'bucket':bucket,})

def share_details(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	return render(request,'blist/share_details.html', {'item':item,})

def register(request):
	if request.user.is_authenticated():
		HttpResponseRedirect('/blist/')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/blist/")
	else:
		form = UserCreationForm()
	return render(request, "blist/register.html", {'form': form,})

# X-Editable Views

@login_required
def xu_desc(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	if request.method == 'POST':
		if request.is_ajax():
			new_desc = request.POST.get('value')
			item.item_desc = new_desc
			item.save()
			return HttpResponse(status=200)

@login_required
def xu_url(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	if request.method == 'POST':
		if request.is_ajax():
			new_url = request.POST.get('value')
			item.item_url = new_url
			item.save()
			return HttpResponse(status=200)

@login_required
def xu_name(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	if request.method == 'POST':
		if request.is_ajax():
			new_name = request.POST.get('value')
			item.item_value = new_name
			item.save()
			return HttpResponse(status=200)

@login_required
def xu_date(request, bucket_id, item_id):
	item = get_object_or_404(Item,pk=item_id)
	if request.method == 'POST':
		if request.is_ajax():
			new_date = request.POST.get('value')
			item.finish = new_date
			item.save()
			return HttpResponse(status=200)
