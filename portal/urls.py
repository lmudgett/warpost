from django.conf.urls import patterns, url

urlpatterns = patterns('portal.views',
    url(r'^$', 'index'),
)