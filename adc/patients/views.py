
from django.shortcuts import redirect, render
from patients.forms import *
from clinic.models import *
from .models import Patient
from .models import *
# importing the necessary libraries
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
#from app1 import models
from doctors.process import html_to_pdf 
from django.template.loader import render_to_string


# Create your views here.
def patland(request):
  p =User.objects.filter(is_patient=True)
  pat = Patient.objects.get(pk=request.user)
  press = pat.prescription_set.all()
  rep = pat.medicalhistory_set.all()
  apt=pat.schedule_set.filter(status='Confirmed').last()
  pendapt=pat.schedule_set.filter(status='Pending').last()
  l=pat.schedule_set.filter(status='Pending').count()
  k=pat.schedule_set.filter(status='Confirmed').count()
  print(l)
  return render(request, 'patland.html', {'p':p, 'press': press, 'rep':rep, 'apt':apt,'pendapt':pendapt,'l':l,'k':k})

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

# def prescription(request, pid):
#   p = Patient.objects.get(pk=pid)
#   press = p.prescription_set.all()
#   return render(request, 'patpres.html', {'press': press})


def createappt(request):
  form=ScheduleForm()
  p = Patient.objects.get(pk=request.user.pk)
  l=p.schedule_set.filter(status='Pending').count()

  if request.method == 'POST':
    form=ScheduleForm(request.POST)
   
  
    if form.is_valid():
      form.instance.patient=p
      form.instance.status='Pending'
      form.save()
      return redirect('patland/')
  context={'form':form,'l':l}
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
        p.gender=request.POST.get("gender")
        p.save()
        return redirect('/patients/info/')

#for pdf
def printPres(request,id):
  p = Patient.objects.get(user_id=request.user)
  data = p.prescription_set.get(pk=id)

  pdf = html_to_pdf('prescription_pdf.html', {'data': data})

  return HttpResponse(pdf, content_type='application/pdf')   