# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-02 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_brand', models.ImageField(default='brandlogo.png', upload_to='img/logo', verbose_name='品牌logo')),
                ('btitle', models.CharField(max_length=30, verbose_name='品牌')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'db_table': 'Brand',
                'verbose_name': '车辆品牌表',
                'verbose_name_plural': '车辆品牌表',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Carinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=30, verbose_name='车名')),
                ('regist_date', models.DateField(verbose_name='上牌时间')),
                ('engineNo', models.CharField(max_length=30, verbose_name='发动机号')),
                ('mileage', models.IntegerField(default=10, verbose_name='公里数')),
                ('maintenance_record', models.CharField(choices=[('true', '是'), ('false', '否')], default='false', max_length=10, verbose_name='维修记录')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='期望售价')),
                ('extractprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成交售价')),
                ('newprice', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='新车价格')),
                ('picture', models.ImageField(default='normal.png', upload_to='img/car', verbose_name='照片')),
                ('formalities', models.CharField(choices=[('true', '是'), ('false', '否')], default='true', max_length=10, verbose_name='手续')),
                ('debt', models.CharField(choices=[('true', '是'), ('false', '否')], default='false', max_length=10, verbose_name='债务')),
                ('promise', models.TextField(null=True, verbose_name='卖家承诺')),
                ('examine', models.CharField(choices=[('1', '审核中'), ('2', '审核通过'), ('3', '审核不通过')], default='1', max_length=30, verbose_name='审核进度')),
                ('isPurchase', models.BooleanField(default=False, verbose_name='是否购买')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('serbran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Brand', verbose_name='车辆型号')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='用户')),
            ],
            options={
                'db_table': 'Carinfo',
                'verbose_name': '车辆信息表',
                'verbose_name_plural': '车辆信息表',
                'ordering': ['-id'],
            },
        ),
    ]
