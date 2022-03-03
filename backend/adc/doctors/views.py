from django.shortcuts import render, redirect
from matplotlib.style import context
from patients.models import *
from clinic.models import *
from .forms import *
# Create your views here.
def patientlist(request):
    p=Patient.objects.all()
    t_p = p.count()
    
    context={'p':p,'t_p':t_p}
    return render(request,'doctors/patient_list.html',context)

def patientinfo(request,pk_t):
    p = Patient.objects.get(id=pk_t)
    mh = p.prescription_set.all()
    medihis = p.medicalhistory_set.all()        
    bi = p.billinfo_set.all()
    sch = p.schedule_set.all()

    
    context= {'p':p,'mh':mh,'medihis':medihis,'bi':bi,'sch':sch}
    return render(request, 'doctors/patient_info.html',context)

def createprescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctors/patlist/')
    context={'form':form}
    return render(request, 'doctors/prescription_form.html',context )
    
def createbillinfo(request):
    form = BillInfoForm()
    if request.method == 'POST':
        form=BillInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctors/patlist/')
    
    context={'form':form}
    return render(request, 'doctors/billinfo_form.html',context )
    