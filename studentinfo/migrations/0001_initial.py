# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc', models.FileField(blank=True, null=True, upload_to='media/upload/%y/%m/%d/')),
                ('inter', models.FileField(blank=True, null=True, upload_to='media/upload/%y/%m/%d/')),
                ('degree', models.FileField(blank=True, null=True, upload_to='media/upload/%y/%m/%d/')),
                ('mca', models.FileField(blank=True, null=True, upload_to='media/upload/%y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('mobile_no', models.IntegerField(max_length=12)),
                ('address', models.TextField(max_length=500)),
                ('roll_no', models.IntegerField(max_length=10)),
                ('d_join_date', models.DateTimeField(blank=True, null=True)),
                ('registration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='studentinfo.Registration')),
            ],
        ),
        migrations.AddField(
            model_name='documents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentinfo.Student'),
        ),
    ]
