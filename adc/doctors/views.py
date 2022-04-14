import os
import datetime
from pipes import Template
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from doctors.filters import *
from patients.models import *
from clinic.models import *
from doctors.models import *
from .forms import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

# importing the necessary libraries
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
#from app1 import models
from .process import html_to_pdf 
from django.template.loader import render_to_string

# Create your views here.
@login_required
def patientlist(request):
    
    p=User.objects.filter(is_patient=True)
    
    t_p = p.count()
    
    context={'p':p,'t_p':t_p}
    return render(request,'doctors/patient_list.html',context)

@login_required
def viewReport(request, id):
    history = MedicalHistory.objects.get(pk=id)
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     remark = history.remarks
    #     report = history.report
    #     patient = history.patient
    #     d = Doctors.objects.get(user_id=request.user)
    #     subject = 'Report of the patient'
    #     email_template_name = 'doctors/report_email.txt' 
    # '''
    #    <html>
    #     <body>
    #      <table>
    #        <tr>
    #            <td style="font-family:Verdana, Geneva, sans-serif; font-weight:400; font-size:15px;">Report:</td>
    #        </tr>
    #        <tr>
    #            <img src="cid:logo.png" />
    #        </tr>
    #        <tr>
    #           <td style="font-family:Verdana, Geneva, sans-serif; font-weight:400; font-size:15px;">Remarks:</td>
    #        </tr>
    #        <tr>
    #           <td style="font-family:Verdana, Geneva, sans-serif; font-weight:400; font-size:15px;">{{remarks}}</td>
    #        </tr>
    #      </table>
    #    </body>
    #   </html>
    #    '''
    #     msg = EmailMultiAlternatives(subject,email_template_name,from_email=settings.EMAIL_HOST_USER,to=[email])

    #     msg.mixed_subtype = 'related'
    #     msg.attach_alternative(email_template_name, "text/html")
    #     img_dir = 'static'
    #     image = report
    #     file_path = open(os.path.join('C:/Users/newadc/ADC-Care/adc', image.url), 'rb')
    #     img = MIMEImage(file_path.read())
    #     file_path.close()
    #     msg.attach(img)
    #     msg.send()
        # c = {
        #     "remark" : remark,
        #     "report": report.url,
        #     "patient": patient,
        #     "doctor": d.dname
        # }
        # email = render_to_string(email_template_name, c)
        # try:
        #  send_mail(subject, email, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        # except BadHeaderError:
        #  return HttpResponse('Invalid header found.')
        # return redirect('reports')
    return render(request, 'doctors/viewreport.html',{'mh': history})

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
    d =Doctors.objects.get(pk=request.user.pk)
    form = PrescriptionForm()
    if request.method == 'POST':
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.instance.doctor=d
            form.save()
            messages.success(request, 'Successfully created prescrption')
            return redirect('/doctors/patlist/')
    context={'form':form}
    return render(request, 'doctors/prescription_form.html',context )

@login_required
def createbillinfo(request):
    d =Doctors.objects.get(pk=request.user.pk)
    form = BillInfoForm()
    if request.method == 'POST':
        form=BillInfoForm(request.POST)

        if form.is_valid():
            form.instance.doctor=d
            paid=form.instance.paid
            amount= form.instance.amount
            form.instance.balance = paid - amount
            form.save()
            messages.success(request, 'Successfully created bill')
            return redirect('/doctors/patlist/')
    
    context={'form':form}
    return render(request, 'doctors/billinfo_form.html',context )


@login_required
def createreport(request):
    form = ReportForm()
    d =Doctors.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form=ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.doctor=d
            form.save()
            messages.success(request, 'Successfully created report')
            return redirect('/doctors/patlist/')
    
    context={'form':form }
    return render(request, 'doctors/report_form.html',context )

@login_required
def home(request):
    s=Schedule.objects.all()
    doc = Doctors.objects.all()
    d = Doctors.objects.get(pk=request.user)
    return render(request, 'doctors/home.html',{'s':s, 'doc': doc,'d':d})


class Manageapt(LoginRequiredMixin,ListView):
    template_name = "doctors/mng.html"
    model = Schedule
    context_object_name= "apt"

    def post(self, request):
        time = request.POST.get("time")
        sch_id = request.POST.get("sch-id")
        apt = Schedule.objects.get(id=sch_id)
        d = apt.scheduleDate
        e = apt.patient.email
        apt.scheduleTime=time
        apt.accepted = True
        apt.accepted_date = datetime.datetime.now()
        apt.save()
        subject = "Appointment Confirmed"
        email_template = "doctors/apt_email.txt"
        c = {
            "date":d,
            "time": time,
        }
        email = render_to_string(email_template, c)
        try:
            send_mail(subject, email, settings.EMAIL_HOST_USER , [e], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, 'A mail has been sent successfully.')
        # return redirect('password_reset_done')
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

    elif request.method == "POST":
        doc = Doctors.objects.get(user_id = request.user)
        doc.dname = request.POST.get("dname")
        doc.email = request.POST.get("email")
        doc.phone = request.POST.get("phone")
        doc.address = request.POST.get("address")
        doc.save()
        return redirect('/doctors/profile/')

@login_required
def printBill(request, id):
    data = BillInfo.objects.get(pk=id)
    # Converting the HTML template into a PDF file
    pdf = html_to_pdf('doctors/billpdf.html', {'data': data})
         
    # rendering the template
    return HttpResponse(pdf, content_type='application/pdf')