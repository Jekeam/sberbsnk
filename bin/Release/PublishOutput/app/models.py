"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Client(models.Model):
    inn = models.CharField( max_length = 12 )
    status = models.CharField( max_length = 20 )
    balance = models.PositiveIntegerField()