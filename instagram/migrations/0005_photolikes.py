# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('liker', models.CharField(max_length=20)),
            ],
        ),
    ]
