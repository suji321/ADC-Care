from django.shortcuts import render
from clinic.models import *
from .models import Patient
# Create your views here.
def patland(request):
  p = Patient.objects.all()
  return render(request, 'patland.html', {'p':p})

def patinfo(request, pid):
  p = Patient.objects.get(id = pid)
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