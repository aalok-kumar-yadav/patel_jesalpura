# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-03 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionclass',
            name='blog_status',
            field=models.CharField(default=True, max_length=5),
            preserve_default=False,
        ),
    ]