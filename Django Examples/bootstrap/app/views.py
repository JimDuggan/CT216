from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext

# Create your views here.
from app.models import getSampleData

def starter(request):
    return render(request,'starter.html')

def marketing(request):
    return render(request,'marketing.html')

def jumbotron(request):
    return render(request,'jumbotron.html')

def test(request):
    return render(request,'test.html')

def home(request):
    return render(request,'home.html')

def option1(request):
    return render(request,'option1.html')

def option2(request):
    return render(request,'option2.html')

def option3(request):
    return render(request,'option3.html')

def option4(request):
    return render(request,'option4.html')

def option5(request):
    # see http://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-tables.php
    data = getSampleData()
    print data
    return render(request,'option5.html', {'cdata' : data})

