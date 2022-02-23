from telnetlib import STATUS
from django.db import models
from doctors.models import Doctors

from patients.models import Patient

# Create your models here.

class MedicalHistory(models.Model):
    remarks = models.CharField(max_length=200, null=True)
    report = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    patient = models.ForeignKey(Patient, null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctors, null=True, on_delete=models.CASCADE)

    def __str__(self):
	    return self.remarks

class Schedule(models.Model):
    STATUS = ( ('Confirmed','Confirmed'), ('Cancel','Cancel'), ('Reschedule','Reschedule'), ('Attended','Attended'))
    scheduleDate = models.DateField()
    scheduleTime = models.TimeField()
    status = models.CharField(null=True, max_length=10, choices=STATUS)
    patient =  models.ForeignKey(Patient, null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctors, null=True, on_delete=models.CASCADE)


class BillInfo(models.Model):
    STATUS=(('Paid','Paid'),('Not Paid','Not Paid'))
    patient =  models.ForeignKey(Patient, null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctors, null=True, on_delete=models.CASCADE)
    bdate=models.DateField()
    payment=models.CharField(max_length=200,null=True)
    status=models.CharField(null=True, max_length=10, choices=STATUS)

