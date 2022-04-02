from django.db import models
from clinic.models import User
# from clinic.models import MedicalHistory

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
    pname=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=4, null=True)
    gender= models.CharField(max_length=6, null=True)
    email=models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=500, null=True)
    phone= models.CharField(max_length=13, null=True)
    # medicalHistory: models.ForeignKey(MedicalHistory, null=True, on_delete= models.SET_NULL)	
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.pname

