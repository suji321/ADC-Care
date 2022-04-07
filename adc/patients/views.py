
from django.shortcuts import redirect, render
from patients.forms import *
from clinic.models import *
from .models import Patient

from .models import *

# Create your views here.
def patland(request):
  p =User.objects.filter(is_patient=True)
  pat = Patient.objects.get(pk=request.user)
  prescriptions = pat.prescription_set.all()
  print(prescriptions)
  return render(request, 'patland.html', {'p':p, 'prescriptions': prescriptions})

def patinfo(request):
  p = Patient.objects.get(user_id=request.user)
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


# @login_required
def profileEdit(request):
    if request.method == "GET":
        p = Patient.objects.get(user_id=request.user)
        return render(request, 'edit.html', {'p': p})
    elif request.method == "POST":
        pname = request.POST.get("pname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        if not pname == "" and not email == "" and not phone == "" and not address == "":
            p = Patient.objects.get(user_id=request.user)
            p.pname = pname
            p.email = email
            p.phone = phone
            p.address = address
            p.save()
            return redirect('/patients/info/')
        p = Patient.objects.get(user_id=request.user)
        return render(request, 'edit.html', {'error': "Some fields are empty", 'p': p})
