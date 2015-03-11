from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from weather_app.models import WeatherData
from weather_app.forms import WeatherDataForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from weather_app.models import UserProfile

def printUserInfo(u):
    print "Printing new user information..."
    print "Username = ", u.username
    print "first_name = ", u.first_name
    print "last_name = ", u.last_name
    print "date_joined =", u.date_joined
    # Get the link to the userprofile
    userp=getattr(u,'userprofile')
    print "Attribute 1", userp.att1
    print "Attribute 2", userp.att2
    print "Attribute 3", userp.att3

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Adding code to show how to create a profile object
            username = request.POST.get('username','')
            password = request.POST.get('password1','')
            print "Username is ", username
            print "Password is ", password
            # Need to get the object that has just been created (User)
            user = auth.authenticate(username=username, password=password)

            # Create a user profile object (see models.py)
            userP = UserProfile()

            # Link the django user object to this profile object
            userP.user = user

            # Add the attributes to the profile (e.g. date of birth, phone, user type, etc)
            userP.att1 = "User Attribute 1"
            userP.att2 = "User Attribute 2"
            userP.att3 = "User Attribute 3"

            # See how you can access the profile data from the user object.
            printUserInfo(user)

            return HttpResponseRedirect("/search-form/")
    else:
        form=UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {'form':form})

def welcome(request):
    return render(request,'welcome.html')

# Displays the search form
@login_required
def search_form(request):
    print request.session
    return render(request,'search.html')

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
    return render(request,
                  'wdata_form.html',
                  {'form':form})

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
            return render(request,
                          'wdata_form.html',{'form':form})

    print("should be calling status...")
    return render(request, 'status.html',{'term':"Saved data to d/base..."})
