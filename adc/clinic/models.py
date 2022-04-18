from django.db import models
#from doctors.models import Doctors
from django.contrib.auth.models import AbstractUser
#from patients.models import Patient
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)

class MedicalHistory(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    patient = models.ForeignKey('patients.Patient', null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctors', null=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=200, null=True)
    report = models.ImageField(upload_to="img/",null=True)
    def __str__(self):
	    return self.remarks

class Schedule(models.Model):
    STATUS = ( ('Confirmed','Confirmed'), ('Cancel','Cancel'), ('Attended','Attended'), ('Pending','Pending'))
    scheduleDate = models.DateField(validators =  [MinValueValidator(datetime.date.today), MaxValueValidator(datetime.date.today() + datetime.timedelta(days=14))])
    scheduleTime = models.TimeField(blank=True, null=True, validators=[MinValueValidator(datetime.time(10,0,0)), MaxValueValidator(datetime.time(18,0,0))])
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    request = models.TextField(blank=True)
    status = models.CharField(null=True, max_length=10, choices=STATUS,blank=True)
    patient =  models.ForeignKey('patients.Patient', null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctors', null=True, on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.patient.pname
    
    class Meta:
        ordering = ["-date_created"]



class BillInfo(models.Model):
    STATUS=(('Paid','Paid'),('Not Paid','Not Paid'))
    patient =  models.ForeignKey('patients.Patient', null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctors', null=True, on_delete=models.CASCADE)
    bdate=models.DateField()
    amount=models.PositiveIntegerField(max_length=200,null=True)
    status=models.CharField(null=True, max_length=10, choices=STATUS)
    balance=models.PositiveIntegerField(max_length=200,null=True)
    paid = models.PositiveIntegerField(max_length=200,null=True)



class Prescription(models.Model):
    #name = models.CharField(max_length=30)
    #frequency = models.CharField(max_length=60)
    direction = models.CharField(max_length=150)
    remarks = models.CharField(max_length=100)
    patient =  models.ForeignKey('patients.Patient', null=True, on_delete= models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctors', null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)