# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_usertypeaccessmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurelocationmodel',
            name='locationId',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='featurelocationmodel',
            name='locationName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usertypeaccessmodel',
            name='accessableFeatures',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
