from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from weather_app.models import WeatherData
from weather_app.forms import WeatherDataForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/search-form/")
    else:
        form=UserCreationForm()

    return render(request,"registration/register.html",{'form':form})

def welcome(request):
    return render(request,'welcome.html')

# Displays the search form
@login_required
def search_form(request):
    print request.session
    return render_to_response('search.html')

# Processes the search request and displays the records
@login_required
def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
    if not term:
        return render_to_response('search.html',{'error':True})
    data = WeatherData.objects.filter(city=term)
    if not data:
        return render(request,'search.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'search_results.html',{'term':term,'wdata':data})

# Displays the weather data form
@login_required
def addWeatherData(request):
    form = WeatherDataForm()
    return render(request,'wdata_form.html',{'form':form})

# Stores the weather data record
@login_required
def storeWeatherData(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)

        if(form.is_valid()):
            cd = form.cleaned_data

            wd = WeatherData(city=cd['city'],
                             country=cd['country'],
                             timestamp=cd['date'],
                             temperature=cd['temperature'])
            wd.save()
            print("Saved weather record...")
        else:
            return render(request,'wdata_form.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Saved data to d/base..."})
