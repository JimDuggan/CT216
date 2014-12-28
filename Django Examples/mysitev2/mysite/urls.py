from django.conf.urls import patterns, include, url

from mysite.views import test,welcome


urlpatterns = patterns('',
    ('^test/',test),
    ('^welcome/',welcome)
)
