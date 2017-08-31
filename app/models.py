"""
Definition of models.
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Statuse(models.Model):
    status = models.CharField(max_length = 20, primary_key=True, default = 'Classic')
    max = models.PositiveIntegerField(default = 0)
    status_desc = models.TextField(max_length = 4000, default='')
    href = models.CharField(default = '#', max_length = 20)

    def __str__(self):
        return self.status


class Balance(models.Model):
    user = models.OneToOneField(User)
    status = models.ForeignKey(Statuse)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class Service(models.Model):
    service_id = models.PositiveIntegerField(primary_key = True)
    service_name = models.CharField(max_length = 50)
    service_desc = models.TextField(max_length = 4000)
    service_price = models.PositiveIntegerField()
    service_statuse = models.ManyToManyField(Statuse)
    service_href = models.CharField(default = '#', max_length = 20)

    def __str__(self):
        return self.service_name