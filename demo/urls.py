from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

if settings.DEBUG:
    from os import path
    urlpatterns = patterns('django.views', (r'^static/(?P<path>.*)$', 'static.serve', {'document_root': path.join(settings.PROJECT_ROOT, 'static') }))
else:
    urlpatterns = patterns('')

from agenda.sitemaps import EventSitemap
from agenda.feeds import EventFeed

from django.contrib.comments.feeds import LatestCommentFeed
    
sitemaps = { 'events' : EventSitemap }

feeds = { 'events'   : EventFeed, 
          'comments' : LatestCommentFeed }

urlpatterns += patterns('',
    (r'^', include('agenda.urls')),

    # Django Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    
    # Comments support
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # Sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Feeds
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)
