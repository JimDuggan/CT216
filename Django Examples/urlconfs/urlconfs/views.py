from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    html="<html><body>It is now %s.</body><html>" % now
    return HttpResponse(html)

def list(request,v1, v2):
    html="<html><body>The values are %s and %s.</body><html>" % (v1,v2)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    html="<html><body>In %s hour(s), is will be %s.</body><html>" % (offset, dt)

    return HttpResponse(html)



