from django.conf.urls import patterns, url

from blist import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^favorites/$', views.favorites, name='favorites'),
	url(r'^(?P<bucket_id>\d+)/$', views.items, name='items'),
	url(r'^(?P<item_id>\d+)/details/$', views.details, name='details'),
	url(r'^(?P<item_id>\d+)/details/edit/$', views.edit_details, name='edit'),
)
