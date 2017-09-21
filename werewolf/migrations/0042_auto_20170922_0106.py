# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0041_auto_20170922_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='charaset',
            field=models.CharField(default='rain', max_length=30),
        ),
        migrations.AlterField(
            model_name='remark',
            name='remarker_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='remark',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resident',
            name='charaset',
            field=models.CharField(default='rain', max_length=30),
        ),
        migrations.AlterField(
            model_name='resident',
            name='job',
            field=models.CharField(default='村人', max_length=100),
        ),
        migrations.AlterField(
            model_name='village',
            name='auther_name',
            field=models.CharField(default='system', max_length=200),
        ),
        migrations.AlterField(
            model_name='village',
            name='charaset',
            field=models.CharField(default='rain', max_length=200),
        ),
        migrations.AlterField(
            model_name='village',
            name='day',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]