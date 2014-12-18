from django.conf.urls import patterns, url

from blist import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^favorites/$', views.index, {'faves':True}, name='favorites'),
	url(r'^shared/$', views.shared_index, name='shared'),
	url(r'^shared/(?P<bucket_id>\d+)/$', views.shared_list, name='shared_list'),
	url(r'^shared/(?P<bucket_id>\d+)/(?P<item_id>\d+)/details/$', views.shared_detail, name='shared_detail'),
	url(r'^(?P<bucket_id>\d+)/$', views.items, name='items'),
	url(r'^(?P<bucket_id>\d+)/share/$', views.share, name='share'),
	url(r'^(?P<bucket_id>\d+)/add_editor/$', views.add_editor, name='add_editor'),		
	url(r'^(?P<bucket_id>\d+)/delete_bl/$', views.delete_bucket, name='delete_bucket'),	
	url(r'^(?P<bucket_id>\d+)/mod_fav_bl/$', views.mod_favorite, name='mod_fav_bl'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/xu_url/$', views.xu_url, name='xu_url'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/xu_name/$', views.xu_name, name='xu_name'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/xu_desc/$', views.xu_desc, name='xu_desc'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/xu_date/$', views.xu_date, name='xu_date'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/delete/$', views.delete_item, name='delete_item'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/finish/$', views.finish, name='finish'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/details/$', views.details, name='details'),
	url(r'^(?P<bucket_id>\d+)/(?P<item_id>\d+)/details/share/$', views.share_details, name='sdetails'),
)
