"""
Definition of urls for ad_track.
"""

from django.conf.urls import include, url
import GenericMetric.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', GenericMetric.views.index, name='index'),
    url(r'^home$', GenericMetric.views.index, name='home'),
    # Examples:
    # url(r'^$', ad_track.views.home, name='home'),
    # url(r'^ad_track/', include('ad_track.ad_track.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
