# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-25 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ardz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='landing_image',
            new_name='screenshot',
        ),
    ]