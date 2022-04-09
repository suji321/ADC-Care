
from django.shortcuts import redirect, render
from patients.forms import *
from clinic.models import *
from .models import Patient

from .models import *

# Create your views here.
def patland(request):
  p =User.objects.filter(is_patient=True)
  pat = Patient.objects.get(pk=request.user)
  press = pat.prescription_set.all()
  return render(request, 'patland.html', {'p':p, 'press': press})

def patinfo(request):
  p = Patient.objects.get(user_id=request.user)
  return render(request, 'patinfo.html', {'p':p})

def patmedhis(request, pid):
  p = Patient.objects.get(pk=pid)
  info = p.medicalhistory_set.all()
  return render(request, 'patmedhis.html', {'info': info}) 

def patbill(request):
  p = Patient.objects.get(pk=request.user)
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
    p = Patient.objects.get(pk=request.user.pk)
    if form.is_valid():
      form.instance.patient=p
      form.save()
      return redirect('patland/')
  context={'form':form}
  return render(request, 'mkapt.html', context)



def profileEdit(request):
    if request.method == "GET":
        p = Patient.objects.get(user_id=request.user)
        return render(request, 'edit.html', {'p': p})
    elif request.method == "POST":
        p = Patient.objects.get(user_id=request.user)
        p.pname = request.POST.get("dname")
        p.email = request.POST.get("email")
        p.phone = request.POST.get("phone")
        p.address = request.POST.get("address")
        p.save()
        return redirect('/patients/info/')
        