from django.contrib import auth
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from datetime import datetime
from app.models import Statuse, Balance, Service

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
        #Статусы
        try:
            statuse = Statuse.objects.all()
        except:
            statuse = None
        #Текущий баланс
        try:
            balance = Balance.objects.get( user_id = request.user.id)
            cur_balance = balance.balance
            #Статус юзера
            cur_status = balance.status_id
        except:
            cur_balance = None
            cur_status = None
        #Следующий статус
        try:
             status = Statuse.objects.get( status = balance.status_id )
             status_max = status.max
             next_status = status_max-cur_balance if status_max-cur_balance > 0 else 0
        except:
            next_status = None
        #Получим список возможных услуг
        try:
            services = Service.objects.filter(service_statuse = cur_status)
        except:
            services = None

        #Текущий статус
        try:
            balance = Balance.objects.get( user_id = request.user.id)
            #Статус юзера
            cur_status = balance.status_id
        except:
            cur_status = None

        #assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/office.html',
            {
                'title':'Кабинет',
                'year':datetime.now().year,
                'header_class':'office',
                'statuse': statuse,
                'cur_balance': cur_balance,
                'cur_status': cur_status,
                'next_status': next_status,
                'services': services,
            }
        )
    raise Http404

def status(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            get_status = request.GET.get('status_id')
            print(str(get_status))
            #Описание статуса
            try:
                get_status_desc = Statuse.objects.filter(status = get_status)
            except:
                get_status_desc = None

            #Получим список возможных услуг
            try:
                services = Service.objects.filter(service_statuse = get_status)
            except:
                services = None

            return render(
            request,
            'app/status.html',
            {
                'title':'Статус',
                'year':datetime.now().year,
                'header_class':'office',
                'get_status_desc': get_status_desc,
                'services': services,
            }
        )
        raise Http404
    raise Http404