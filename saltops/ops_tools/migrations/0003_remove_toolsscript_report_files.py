# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops_tools', '0002_toolsscript_report_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolsscript',
            name='report_files',
        ),
    ]
