from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pingotron.views.home', name='home'),
    (r'^', include('pingotron.record.urls')),

    # About and Contact
    #(r'^', include('livingcitymap.about.urls')),

    #(r'^user/', include('livingcitymap.accounts.urls')),

    #(r'^', include('livingcitymap.events.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^admin/', include(admin.site.urls)),
     #url(r'^admin2/', include(admin.site.urls)),
)
