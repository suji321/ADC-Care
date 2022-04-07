import datetime
from pipes import Template
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from doctors.filters import *
from patients.models import *
from clinic.models import *
from doctors.models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def patientlist(request):
    
    p=User.objects.filter(is_patient=True)
    
    t_p = p.count()
    
    context={'p':p,'t_p':t_p}
    return render(request,'doctors/patient_list.html',context)

@login_required
def patientinfo(request,pk_t):
    p = Patient.objects.get(user_id=pk_t)
    mh = p.prescription_set.all()
    medihis = p.medicalhistory_set.all()        
    bi = p.billinfo_set.all()
    sch = p.schedule_set.all()
    bfilter = BillFilter(request.GET,queryset=bi)
    bi = bfilter.qs
    medfilter = MedhisFilter(request.GET,queryset=medihis)
    medihis = medfilter.qs
    schfilter=SchFilter(request.GET,queryset=sch)
    sch = schfilter.qs
    prescfilter=PrescriptionFilter(request.GET,queryset=mh)
    mh=prescfilter.qs

    context= {'p':p,'mh':mh,'medihis':medihis,'bi':bi,'sch':sch,'bfilter':bfilter,'medfilter':medfilter,'schfilter':schfilter,'prescfilter':prescfilter}
    return render(request, 'doctors/patient_info.html',context)

@login_required
def createprescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctors/patlist/')
    context={'form':form}
    return render(request, 'doctors/prescription_form.html',context )

@login_required
def createbillinfo(request):
    form = BillInfoForm()
    if request.method == 'POST':
        form=BillInfoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/doctors/patlist/')
    
    context={'form':form}
    return render(request, 'doctors/billinfo_form.html',context )


@login_required
def createreport(request):
    form = ReportForm()
    if request.method == 'POST':
        form=ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctors/patlist/')
    
    context={'form':form}
    return render(request, 'doctors/report_form.html',context )


def home(request):
    s=Schedule.objects.all()
    doc = Doctors.objects.all()
    return render(request, 'doctors/home.html',{'s':s, 'doc': doc})


class Manageapt(LoginRequiredMixin,ListView):
    template_name = "doctors/mng.html"
    model = Schedule
    context_object_name= "apt"

    def post(self, request):
        time = request.POST.get("time")
        sch_id = request.POST.get("sch-id")
        apt = Schedule.objects.get(id=sch_id)
        apt.scheduleTime=time
        apt.accepted = True
        apt.accepted_date = datetime.datetime.now()
        apt.save()

        return HttpResponseRedirect(request.path)

    
    def get_context_data(self,*args, **kwargs):
       
        context= super().get_context_data(**kwargs)
        apt = Schedule.objects.all()
        context.update({
            
            "title":"Manage Appointment"

        })
        return context


def login(request):
    return render(request, 'doctors/login.html')

def register(request):
    return render(request, 'doctors/register.html')

@login_required
def profile(request):
    doc = Doctors.objects.get(user_id=request.user)
    return render(request, 'doctors/profile.html', {'doc': doc})

@login_required
def profileEdit(request):
    if request.method == "GET":
        doc = Doctors.objects.get(user_id=request.user)
        return render(request, 'doctors/edit.html', {'doc': doc})
