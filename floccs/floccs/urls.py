from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from floccs.views import IndexView, logout_view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^', include('CustomUser.urls')),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^inbox/', include('Message.urls')),
    url(r'^logout/', logout_view, name = 'logout'),
    url(r'^events/', include('Event.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))