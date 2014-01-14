from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from floccs.views import IndexView, logout_view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^', include('CustomUser.urls')),
    url(r'^logout/', logout_view, name = 'logout'),


    url(r'^admin/', include(admin.site.urls)),
)
