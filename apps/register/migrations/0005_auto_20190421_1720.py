# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-21 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20190419_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='n_Earnleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_commutingleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_dutyleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_halfleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_maternityleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_paternityleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_sickleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='n_specialleave',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='user',
            name='u_Earnleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_commutingleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_dutyleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_halfleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_maternityleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_paternityleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_sickleave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='u_specialleave',
            field=models.IntegerField(default=0),
        ),
    ]
