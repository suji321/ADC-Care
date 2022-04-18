from . import views
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', views.home,name='home'),
    path('patlist/', views.patientlist,name='patient'),
    path('pat/<str:pk_t>/', views.patientinfo,name="pat"),
    path('create_prescription/',views.createprescription,name="crtprc"),
    path('attend_apt/', Attendedapt.as_view(),name="atdapt"),
    path('create_report/', views.createreport, name='crtreport'),
    path('billinfo_form/',views.createbillinfo,name="crtbill"),
    path('manage-appt/', Manageapt.as_view() ,name="manage-appt"),
    # path('login/', views.login, name="login"),
    # path('register/', views.register, name="register"),
    path('profile/', views.profile,name="profile"),
    path('profileEdit/', views.profileEdit,name="profileEdit"),
    path('reports/<str:id>', views.viewReport,name="reports"),
    path('pdf/<str:id>/', views.printBill, name='billpdf'),
    
]