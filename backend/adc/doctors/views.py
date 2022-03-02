from django.shortcuts import render
from patients.models import *
from clinic.models import *
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

    
    context= {'p':p,'mh':mh,'medihis':medihis,'bi':bi}
    return render(request, 'doctors/patient_info.html',context)

