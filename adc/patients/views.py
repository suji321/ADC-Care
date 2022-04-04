
from django.shortcuts import redirect, render
from patients.forms import *
from clinic.models import *
from .models import Patient

from .models import *

# Create your views here.
def patland(request):
  p =User.objects.filter(is_patient=True)
  return render(request, 'patland.html', {'p':p})

def patinfo(request, pid):
  p = Patient.objects.get(user_id=pid)
  return render(request, 'patinfo.html', {'p':p})

def patmedhis(request, pid):
  p = Patient.objects.get(pk=pid)
  info = p.medicalhistory_set.all()
  return render(request, 'patmedhis.html', {'info': info}) 

def patbill(request, pid):
  p = Patient.objects.get(pk=pid)
  bill = p.billinfo_set.all()
  return render(request, 'patbill.html', {'bill':bill})

def prescription(request, pid):
  p = Patient.objects.get(pk=pid)
  press = p.prescription_set.all()
  return render(request, 'patpres.html', {'press': press})


def createappt(request):
  form=ScheduleForm()
  if request.method == 'POST':
    form=ScheduleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('patland/')
    
  context={'form':form}
  return render(request, 'mkapt.html',context )
