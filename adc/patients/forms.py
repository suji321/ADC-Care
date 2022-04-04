from pyexpat import model
from attr import field
from django .forms import ModelForm
from .models import*
from patients.models import *
from clinic.models import *

class ScheduleForm(ModelForm):
    class Meta:
        model=Schedule
        fields=['request','scheduleDate','patient','doctor']