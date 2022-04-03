from unicodedata import name
from doctors import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('patlist/', views.patientlist,name="patlist"),
    path('profile/', views.profile,name="profile"),
    path('profileEdit/', views.profileEdit,name="profileEdit"),
    path('pat/<str:pk_t>/', views.patientinfo,name="pat"),
    path('create_prescription/',views.createprescription,name="crtprc"),
    path('billinfo_form/',views.createbillinfo,name="crtbill")

    
]