# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 23:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('werewolf', '0034_auto_20170921_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='auther',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
