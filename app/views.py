from django.contrib import auth
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/office.html')
        else:
            return render(request, 'app/index.html', {'username':username, 'errors': True})
    raise Http404


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/')
    raise Http404


def office(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/office.html',
        {
            'title':'Офис',
            'year':datetime.now().year,
        }
    )
