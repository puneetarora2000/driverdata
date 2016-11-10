from __future__ import unicode_literals

from datetime import time

from django.db import models
import random
import string
# Create your models here.

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class Driver(models.Model):
    DriverID = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=30)
    FullAddress = models.TextField(max_length=254)
    State = models.CharField(max_length=254)
    City = models.CharField(max_length=254)
    Driver_History = models.TextField()
    RegisterDriver_RemoteMonitoring = models.BooleanField()
    DriverDocs = models.FileField(upload_to = get_upload_file_name)
    def __unicode__(self):
        return str(self.FullName)

class DriverCab(models.Model):
    DirverID = models.ForeignKey(Driver,default=1,blank=True)
    CabID = models.AutoField(primary_key=True)
    CabRegistration = models.CharField(max_length=30)
    EngineID = models.TextField(max_length=254)
    IsOwner = models.TextField()
    LastUpdate = models.DateField(auto_created=True)
    def __unicode__(self):
        return str(self.CabID)

class RegisterDevices(models.Model):
    RegistrationID = models.AutoField(primary_key=True)
    DriverID = models.ForeignKey(Driver,default=1,blank=True)
    SugarMonitoringDevice = models.BooleanField(default=False)
    WorkOutMachineDevice = models.BooleanField(default=True)
    PulseMonitor = models.BooleanField(default=False)
    TemperatureMonitor =  models.BooleanField(default=False)
    SleepPatternsMonitor = models.BooleanField(default=True)
    GulcoseMonitoringDeviceID = models.CharField(max_length=200)
    WorkOutMachineDeviceID = models.CharField(max_length=200)
    PulseMonitorID = models.CharField(max_length=200)
    TemperatureMonitorID = models.CharField(max_length=200)
    SleepPatternsDeviceID = models.CharField(max_length=200)
    PollingIntervalInMilliSec = models.IntegerField(default=10)
    LastUpdate = models.DateField(auto_created=True)
    def __unicode__(self):
        return str(self.DriverID)


    def save(self,*args,**kwargs):
        random1 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        self.GulcoseMonitoringDeviceID = 'GM' + str(self.Patient_ID) + random1
        random2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        self.WorkOutMachineDeviceID = 'WM' + str(self.Patient_ID) + random2
        random3 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        self.PulseMonitorID = 'PM' + str(self.Patient_ID) + random3
        random4 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        self.TemperatureMonitorTM = 'TM' + str(self.Patient_ID) + random4
        random5 = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        self.SleepPatternsDeviceID  = 'SPM' + str(self.Patient_ID) + random5
        super(RegisterDevices, self).save(*args, **kwargs)



class DriverData(models.Model):
    DataID = models.AutoField(primary_key=True)
    DriverID = models.ForeignKey(Driver,default=1,blank=True)
    CabID = models.ForeignKey(DriverCab,default=1,blank=True)
    DataOfReading = models.DateTimeField(blank=True,verbose_name="Date of Reading")
    SugarMonitoringDeviceReading = models.FloatField(default=0)
    WorkOutMachineDeviceReading = models.FloatField(default=0)
    PulseMonitorReading = models.FloatField(default=0)
    TemperatureMonitorReading =  models.FloatField(default=0)
    SleepPatternsMonitorReading = models.FloatField(default=0)
    LastUpdate = models.DateField(auto_created=True)
    def __unicode__(self):
        return self.DriverID
