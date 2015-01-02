from django import forms

class WeatherDataForm(forms.Form):
    country = forms.CharField(label="Country")
    city     = forms.CharField(label="City")
    date     = forms.DateTimeField(label="Date")
    temperature = forms.DecimalField(decimal_places=None,
                                     label="Temperature")

