from django.conf.urls import patterns, url

from blist import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^favorites/$', views.favorites, name='favorites'),
	url(r'^ajax_add/$', views.ajax_add, name='ajax_add'),
	url(r'^(?P<bucket_id>\d+)/$', views.items, name='items'),
	url(r'^(?P<bucket_id>\d+)/share/$', views.share, name='share'),
	url(r'^(?P<bucket_id>\d+)/delete_bl/$', views.delete_bucket, name='delete_bucket'),	
	url(r'^(?P<bucket_id>\d+)/mod_fav_bl/$', views.mod_favorite, name='mod_fav_bl'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/delete/$', views.delete_item, name='delete_item'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/finish/$', views.finish, name='finish'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/qedit/$', views.qedit, name='qedit'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/details/$', views.details, name='details'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/details/edit/$', views.edit_details, name='edit'),
)
