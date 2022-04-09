from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from patients.models import Patient
from .models import User, BillInfo
from doctors.models import Doctors
from django import forms

class PatientSignUpForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.CharField(required=True)
    email= forms.EmailField(required=True)
    address= forms.CharField()
    phone = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) is not 10:
    #         raise forms.ValidationError('Phone number must have 10 digits')
    #     return phone

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not validate_email(email, verify=True):
    #         raise forms.ValidationError('Invalid email')
    #     return email
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.email = self.cleaned_data.get('email')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.pname = self.cleaned_data.get('full_name')
        patient.age = self.cleaned_data.get('age')
        patient.gender = self.cleaned_data.get('gender')
        patient.email = self.cleaned_data.get('email')
        patient.address = self.cleaned_data.get('address')
        patient.phone = self.cleaned_data.get('phone')
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    ROLE = (
			('Doctor', 'Doctor'),
			('Staff', 'Staff'),
			
			)
    full_name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE)
    specialisation = forms.CharField(required=True)
    address = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) is not 10:
    #         raise forms.ValidationError('Phone number must have 10 digits')
    #     return phone

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not validate_email(email, verify=True):
    #         raise forms.ValidationError('Invalid email')
    #     return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff - True
        user.email = self.cleaned_data.get('email')
        user.save()
        doctor = Doctors.objects.create(user=user)
        doctor.dname = self.cleaned_data.get('full_name')
        doctor.phone = self.cleaned_data.get('phone')
        doctor.email = self.cleaned_data.get('email')
        doctor.role = self.cleaned_data.get('role')
        doctor.specialisation = self.cleaned_data.get('specialisation')
        doctor.address = self.cleaned_data.get('address')
        doctor.save()
        return user

# class BillForm(forms.ModelForm):
#     class Meta:
#      model = BillInfo
#      fields = ('bdate','payment','status','patient','doctor')

#      widgets = {
#         'bdate': forms.DateInput(),
#         'doctor': forms.Select(),
#         'patient': forms.Select(),
#         'payment': forms.TextInput(),
#         'status': forms.Select(attrs={'class': 'form-control'})
#      }