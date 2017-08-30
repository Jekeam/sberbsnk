from django.contrib import auth
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from datetime import datetime
from app.models import Statuse
from app.models import Balance

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
            'header_class':'landing',
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
            return render(request, 
                          'app/index.html', 
                          {
                              'username':username, 
                              'errors': True,
                              'header_class':'landing'
                          })
    raise Http404


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/')
    raise Http404


def office(request):
    if request.user.is_authenticated():
        try:
            statuse = Statuse.objects.all()
        except:
            statuse = None
        try:
            balance = Balance.objects.get( user_id = request.user.id)
        except:
            balance = None
        try:
            cur_status = Statuse.objects.get( status = balance.status_id )
        except:
            statuse = None
        #assert isinstance(request, HttpRequest)
        print(balance.balance)
        print(cur_status.max)
        return render(
            request,
            'app/office.html',
            {
                'title':'Кабинет',
                'year':datetime.now().year,
                'header_class':'office',
                'statuse': statuse,
                'balance': balance,
                'next_status': cur_status.max-balance.balance,
            }
        )
    raise Http404