from doctors import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('patlist/', views.patientlist),
    path('pat/<str:pk_t>/', views.patientinfo,name="pat"),
]