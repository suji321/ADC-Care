from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from patients.models import Patient
from .models import User, BillInfo
from doctors.models import Doctors
from django import forms
#from django.core.validators import validate_email
from .token import account_activation_token
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import BadHeaderError, send_mail

class PatientSignUpForm(UserCreationForm):
    GENDER = (('Male','Male'),
    ('Female','Female'),
    ('Other','Other'))
    full_name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER)
    email= forms.EmailField(required=True)
    address= forms.CharField()
    phone = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(str(phone)) != 10:
            raise forms.ValidationError('Phone number must have 10 digits')
        return phone

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not validate_email(email):
    #         raise forms.ValidationError('Invalid email')
    #     return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_active = False
        user.is_patient = True
        user.email = self.cleaned_data.get('email')
        user.save()
        email_template_name = 'acc_activation.txt'
        mail_subject = 'Activation link has been sent to your email id'
        c = {
            'user': user,
            'domain': '127.0.0.1:8000',
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'site_name':'Website',
            'protocol': 'http',
        }
        email = render_to_string(email_template_name, c)
        send_mail(mail_subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
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

    GENDER = (('Male','Male'),
    ('Female','Female'),
    ('Other','Other'))
    full_name = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE)
    specialisation = forms.CharField(required=True)
    address = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(str(phone)) != 10:
            raise forms.ValidationError('Phone number must have 10 digits')
        return phone

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not validate_email(email):
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
        doctor.gender = self.cleaned_data.get('gender')
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