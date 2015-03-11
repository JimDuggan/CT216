from django.db import models

# Create your models here.


class WeatherData(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=3, decimal_places=0)


    def __unicode__(self):
        return self.city


# New class added which allows us to link profile data back to the user object
# It's a one-to-one link. All profile info that's not contained in the default can
# be added here.

class UserProfile(models.Model):
     user = models.OneToOneField('auth.User')
     att1 = models.CharField(max_length=30)
     att2 = models.CharField(max_length=30)
     att3 = models.CharField(max_length=30)

