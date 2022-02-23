from django.db import models

# Create your models here.
class Patient(models.Model):
    pname=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=4, null=True)
    gender= models.CharField(max_length=6, null=True)
    email=models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=500, null=True)
    phone= models.CharField(max_length=13, null=True)
    # medicalHistory: models.CharField(max_length=200, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.pname