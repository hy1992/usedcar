# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-02 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0001_initial'),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='车辆信息')),
                ('picture', models.ImageField(default='normal.png', upload_to='', verbose_name='照片')),
                ('price', models.CharField(max_length=30, verbose_name='成交价格')),
                ('newprice', models.CharField(max_length=30, verbose_name='新车价格')),
                ('mileage', models.CharField(max_length=30, verbose_name='公里数')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Carinfo', verbose_name='车辆')),
                ('suser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='买家')),
            ],
            options={
                'db_table': 'Cart',
                'verbose_name': '购物表',
                'verbose_name_plural': '购物表',
            },
        ),
    ]
