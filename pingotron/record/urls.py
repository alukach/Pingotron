from django.conf.urls import patterns, include, url

urlpatterns = patterns('pingotron.record.views',
    url(r'^$', 'overview'),
    url(r'^game/$', 'create_game'),
)
