from django.conf.urls import patterns, include, url

from django.contrib import admin
from urlconfs.views import hello, current_datetime, hours_ahead
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'urlconfs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^hello/$',hello),
    url('^time/$',current_datetime),
    url('^time/plus/(\d{1,2})/$',hours_ahead),
    url('^test/(\d{3,3})(\d{7,7})/$',list),
    url(r'^admin/', include(admin.site.urls)),
)
