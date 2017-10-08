# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20171004_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureLocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationId', models.CharField(default='', max_length=50)),
                ('locationName', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userTypeAccessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(default='', max_length=10)),
                ('accessableFeatures', models.CharField(default='', max_length=100000)),
            ],
        ),
    ]
