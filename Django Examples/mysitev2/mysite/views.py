from django.shortcuts import render_to_response
from time import strftime, gmtime

def welcome(request):
    print request.get_host()
    return render_to_response('welcome.html')

def test(request):
    orderRec = {'name'         : 'John',
                'order_number' : '1111111FFFFF',
                'date'         : strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                'items'        : [{'ID': 'MX101','Description':'Laptop','Qty':1},
                                 {'ID': 'MX102','Description':'Mouse','Qty':2}]
               }
    return render_to_response('test.html', orderRec)





