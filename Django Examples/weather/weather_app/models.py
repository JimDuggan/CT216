from django.db import models

# Create your models here.


class WeatherData(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=3, decimal_places=0)


    def __unicode__(self):
        return self.city
