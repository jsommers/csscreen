# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0004_auto_20170526_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='groups',
        ),
        migrations.AlterField(
            model_name='screen',
            name='lastfetch',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.DeleteModel(
            name='ScreenGroup',
        ),
    ]