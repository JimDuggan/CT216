from django.contrib import admin

# Register your models here.

from weather_app.models import WeatherData
admin.site.register(WeatherData)
