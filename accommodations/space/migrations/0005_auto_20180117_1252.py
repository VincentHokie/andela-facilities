# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_auto_20180117_0924'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccomodationOccupant',
            new_name='Occupant',
        ),
        migrations.RenameModel(
            old_name='AccomodationRoom',
            new_name='Room',
        ),
        migrations.RenameModel(
            old_name='AccomodationSpace',
            new_name='Space',
        ),
    ]
