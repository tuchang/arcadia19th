# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0037_auto_20170922_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remark',
            old_name='character_img_url',
            new_name='icon_url',
        ),
        migrations.RenameField(
            model_name='resident',
            old_name='character_img_url',
            new_name='icon_url',
        ),
        migrations.RenameField(
            model_name='village',
            old_name='character_img_url',
            new_name='icon_url',
        ),
    ]
