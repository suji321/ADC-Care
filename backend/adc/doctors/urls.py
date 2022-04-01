from doctors import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('home/', views.home),
    path('patlist/', views.patientlist),
    path('pat/<str:pk_t>/', views.patientinfo,name="pat"),
    path('create_prescription/',views.createprescription,name="crtprc"),
    path('billinfo_form/',views.createbillinfo,name="crtbill")

    
]