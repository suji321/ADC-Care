from django .forms import ModelForm
from .models import*
from patients.models import *
from clinic.models import *

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

class BillInfoForm(ModelForm):
    class Meta:
        model = BillInfo
        fields = '__all__'
        