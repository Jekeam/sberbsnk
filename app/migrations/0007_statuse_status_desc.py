# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_service_service_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuse',
            name='status_desc',
            field=models.TextField(default='', max_length=4000),
        ),
    ]
