from django.conf.urls import patterns, url

from blist import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<bucket_id>\d+)/$', views.items, name='items'),
)