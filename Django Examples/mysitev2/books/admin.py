from django.contrib import admin

# Register your models here.

from weather_app.models import Wea

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)

