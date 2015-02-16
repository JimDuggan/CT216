from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('app.views',
    # Examples:
    # url(r'^$', 'bootstrap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^starter/$', 'starter'),
    url(r'^marketing/$', 'marketing'),
    url(r'^jumbotron/$', 'jumbotron'),
    url(r'^test/$', 'test'),
    url(r'^home/$', 'home'),
    url(r'^option1/$', 'option1'),
    url(r'^option2/$', 'option2'),
    url(r'^option3/$', 'option3'),
    url(r'^option4/$', 'option4'),
    url(r'^option5/$', 'option5'),
    url(r'^admin/', include(admin.site.urls)),
)
