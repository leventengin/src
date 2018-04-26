# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0003_auto_20180329_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memnuniyet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_no', models.CharField(max_length=20)),
                ('oy', models.CharField(max_length=1)),
                ('sebep', models.CharField(max_length=2)),
                ('gelen_tarih', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
