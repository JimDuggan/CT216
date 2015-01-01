from django.conf.urls import patterns, include, url

from django.contrib import admin
from weather_app.views import search_form, search,addWeatherData,storeWeatherData,register,welcome
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', welcome),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^add_record/$',addWeatherData),
    url(r'^add_wdata/$',storeWeatherData),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',welcome),
)
