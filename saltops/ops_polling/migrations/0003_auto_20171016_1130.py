# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops_polling', '0002_auto_20171016_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingscript',
            name='tool_run_type',
            field=models.IntegerField(choices=[(0, 'SaltState'), (1, 'Shell'), (2, 'PowerShell'), (3, 'Python'), (4, 'Salt命令'), (5, 'Windows批处理')], default=1, verbose_name='脚本类型'),
        ),
        migrations.AlterField(
            model_name='pollingscript',
            name='tool_script',
            field=models.TextField(null=True, verbose_name='脚本'),
        ),
    ]
