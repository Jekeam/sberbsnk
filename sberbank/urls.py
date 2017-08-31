"""
Definition of urls for sberbank.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
#from app.models import Statuse, Balance, Statuse
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login', app.views.login),
    url(r'^user/logout', app.views.logout),
    url(r'^office', app.views.office),
    url(r'^status/', app.views.status),
]
