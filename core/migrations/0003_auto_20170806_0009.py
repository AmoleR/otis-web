# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170805_2322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Handout',
            new_name='Unit',
        ),
    ]
