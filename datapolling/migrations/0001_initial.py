# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-10 11:57
from __future__ import unicode_literals

import datapolling.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('DriverID', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=30)),
                ('FullAddress', models.TextField(max_length=254)),
                ('State', models.CharField(max_length=254)),
                ('City', models.CharField(max_length=254)),
                ('Driver_History', models.TextField()),
                ('RegisterDriver_RemoteMonitoring', models.BooleanField()),
                ('DriverDocs', models.FileField(upload_to=datapolling.models.get_upload_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='DriverCab',
            fields=[
                ('LastUpdate', models.DateField(auto_created=True)),
                ('CabID', models.AutoField(primary_key=True, serialize=False)),
                ('CabRegistration', models.CharField(max_length=30)),
                ('EngineID', models.TextField(max_length=254)),
                ('IsOwner', models.TextField()),
                ('DirverID', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='datapolling.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverData',
            fields=[
                ('LastUpdate', models.DateField(auto_created=True)),
                ('DataID', models.AutoField(primary_key=True, serialize=False)),
                ('DataOfReading', models.DateTimeField(blank=True, verbose_name='Date of Reading')),
                ('SugarMonitoringDeviceReading', models.FloatField(default=0)),
                ('WorkOutMachineDeviceReading', models.FloatField(default=0)),
                ('PulseMonitorReading', models.FloatField(default=0)),
                ('TemperatureMonitorReading', models.FloatField(default=0)),
                ('SleepPatternsMonitorReading', models.FloatField(default=0)),
                ('CabID', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='datapolling.DriverCab')),
                ('DriverID', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='datapolling.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterDevices',
            fields=[
                ('LastUpdate', models.DateField(auto_created=True)),
                ('RegistrationID', models.AutoField(primary_key=True, serialize=False)),
                ('SugarMonitoringDevice', models.BooleanField(default=False)),
                ('WorkOutMachineDevice', models.BooleanField(default=True)),
                ('PulseMonitor', models.BooleanField(default=False)),
                ('TemperatureMonitor', models.BooleanField(default=False)),
                ('SleepPatternsMonitor', models.BooleanField(default=True)),
                ('GulcoseMonitoringDeviceID', models.CharField(max_length=200)),
                ('WorkOutMachineDeviceID', models.CharField(max_length=200)),
                ('PulseMonitorID', models.CharField(max_length=200)),
                ('TemperatureMonitorID', models.CharField(max_length=200)),
                ('SleepPatternsDeviceID', models.CharField(max_length=200)),
                ('PollingIntervalInMilliSec', models.IntegerField(default=10)),
                ('DriverID', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='datapolling.Driver')),
            ],
        ),
    ]
