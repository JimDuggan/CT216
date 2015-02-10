from django.conf.urls import patterns, include, url

from django.contrib import admin
from app.views import starter, marketing, jumbotron, test
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bootstrap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^starter/$', starter),
    url(r'^marketing/$', marketing),
    url(r'^jumbotron/$', jumbotron),
    url(r'^test/$', test),
    url(r'^admin/', include(admin.site.urls)),
)
