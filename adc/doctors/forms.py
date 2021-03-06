from cProfile import label
from pyexpat import model
from django import forms
from django .forms import ModelForm
from .models import*
from patients.models import *
from clinic.models import *

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ('patient','remarks','direction')

        widgets = {
        'doctor': forms.HiddenInput(),
        'patient': forms.Select(),
        'remarks':forms.TextInput(),
        'direction': forms.TextInput(),
        
        
        }

        labels={
            'direction':'Medicine and Dosage (Morning Afternoon Night) (Number of Days)'
        }

class BillInfoForm(ModelForm):
    class Meta:
        model = BillInfo
        fields = ('patient','bdate','amount','paid','status')

        widgets = {
        'doctor': forms.HiddenInput(),
        'patient': forms.Select(),
        'bdate': forms.DateInput(attrs={'type': 'date'}),
        'amount': forms.NumberInput(),
        'paid': forms.NumberInput(),
        'status': forms.Select(attrs={'class': 'form-control'})
     }
     
        labels = {
           'bdate': 'Billing Date'
       }


class DoctorUpdateForm(ModelForm):
    class Meta:
        model = Doctors
        fields = ('dname', 'email', 'phone', 'address')

class ReportForm(ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ('patient','remarks','report')

        widgets = {
        'report': forms.FileInput(),
        
        'patient': forms.Select(),
        'remarks': forms.TextInput(),
     }