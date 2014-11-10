from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from blist import views

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^logout/', logout, {'next_page': '/login/'}),
    url(r'^register/', views.register),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blist/', include('blist.urls', namespace="blist")),
	url(r'^delete/(?P<item_id>\d+)/$', views.delete_item, name='delete_item'),
	url(r'^delete_bl/(?P<bucket_id>\d+)/$', views.delete_bucket, name='delete_bucket'),
)
