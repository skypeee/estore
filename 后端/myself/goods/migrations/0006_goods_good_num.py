# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-24 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_goods_good_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='good_num',
            field=models.IntegerField(default=999, verbose_name='商品数量'),
        ),
    ]
