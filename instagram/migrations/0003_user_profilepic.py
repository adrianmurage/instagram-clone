# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilepic',
            field=models.CharField(default='', max_length=255),
        ),
    ]
