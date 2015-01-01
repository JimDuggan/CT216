from django.conf.urls import patterns, include, url
from django.contrib import admin

from bank.views import test,welcome,books

admin.autodiscover()

urlpatterns = patterns('',
    ('^test/',test),
    ('^welcome/',welcome),
    ('^books/',books),
    (r'^admin/',include(admin.site.urls)),
)
