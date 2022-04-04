from cProfile import label
from django import forms
from django .forms import ModelForm
from .models import*
from patients.models import *
from clinic.models import *

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

        widgets = {
        'doctor': forms.Select(),
        'patient': forms.Select(),
        'remark':forms.TextInput(),
        'direction': forms.TextInput(),
        
        
        }

        labels={
            'direction':'Medicine and Dosage (Morning Afternoon Night) (Number of Days)'
        }

class BillInfoForm(ModelForm):
    class Meta:
        model = BillInfo
        fields = ('bdate','payment','status','patient','doctor')

        widgets = {
        'bdate': forms.DateInput(),
        'doctor': forms.Select(),
        'patient': forms.Select(),
        'payment': forms.TextInput(),
        'status': forms.Select(attrs={'class': 'form-control'})
     }
        