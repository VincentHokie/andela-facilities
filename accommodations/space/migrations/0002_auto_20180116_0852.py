# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccomodationOccupants',
            new_name='AccomodationOccupant',
        ),
    ]
