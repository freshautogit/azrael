# subject
# office
# ticketText
# userFile[]
# username
# email
# phone
# subPhone
# localIp



from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

import testCore

# Create your views here.
def first(request):
    if request.method == 'POST':
        #x = testCore.test(request.POST['textField'])
        x = testCore.createTask('185.216.81.72', request.POST['textField'], '')
    else:
        x = 0
    return render(request, 'yptemptest/index.html', {'x' : x})

def index(request):
    if request.method == 'POST':
        #x = testCore.test(request.POST['textField'])
        x = testCore.createTask('185.216.81.72', request.POST['textField'], '')
    else:
        x = 0
    return render(request, 'helpform/index.html', {'x' : x})

def success(request):
    if request.method == 'POST':
        key = testCore.accept_task(request, get_client_ip(request))
    return render(request, 'helpform/index.html', {'result': key})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip