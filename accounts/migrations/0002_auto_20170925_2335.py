# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userID',
            new_name='user',
        ),
    ]
