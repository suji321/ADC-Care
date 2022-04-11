from django.db import models
from clinic.models import User
from django.core.validators import RegexValidator
# from clinic.models import MedicalHistory

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
    pname=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=4, null=True)
    gender= models.CharField(max_length=6, null=True)
    email=models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=500, null=True)
    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    phone = models.CharField('Phone',validators =[phone_regex], max_length=10, unique = True,null=True)
    
    # medicalHistory: models.ForeignKey(MedicalHistory, null=True, on_delete= models.SET_NULL)	
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.pname
