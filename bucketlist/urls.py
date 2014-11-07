from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from blist.views import register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bucketlist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', login),
    url(r'^logout/', logout, {'next_page': '/login/'}),
    url(r'^register/', register),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blist/', include('blist.urls', namespace="blist")),
)
