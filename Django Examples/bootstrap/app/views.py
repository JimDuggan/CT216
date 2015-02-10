from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext

# Create your views here.

def starter(request):
    return render(request,'starter.html')

def marketing(request):
    return render(request,'marketing.html')

def jumbotron(request):
    return render(request,'jumbotron.html')


def test(request):
    return render(request,'test.html')