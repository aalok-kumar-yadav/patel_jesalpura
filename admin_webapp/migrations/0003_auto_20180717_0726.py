# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_webapp', '0002_sessionclass_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_class',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
