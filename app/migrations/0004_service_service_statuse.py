# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_statuse',
            field=models.ManyToManyField(to='app.Statuse'),
        ),
    ]