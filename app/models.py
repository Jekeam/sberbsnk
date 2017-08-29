"""
Definition of models.
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Statuse(models.Model):
    status = models.CharField(max_length = 20, primary_key=True)

    def __str__(self):
        return self.status


class Balance(models.Model):
    user = models.OneToOneField(User)
    status = models.ForeignKey(Statuse)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user.username)