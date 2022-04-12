from django import forms
from django.forms import ModelForm
from .models import*
from patients.models import *
from clinic.models import *

class ScheduleForm(ModelForm):
    class Meta:
        model=Schedule
        fields=['request','scheduleDate','doctor']

        widgets = {
        'scheduleDate': forms.SelectDateWidget(),
       
        'doctor': forms.Select(),
       
     }