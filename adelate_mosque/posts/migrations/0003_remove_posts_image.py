# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170519_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]
