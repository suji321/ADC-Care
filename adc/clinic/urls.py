from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('patientregister/', views.patient_register.as_view(), name='patientregister'),
    path('doctorregister/', views.doctor_register.as_view(), name='doctorregister'),
    path('login/', views.login_request, name='login'),
    path('loggedin/', views.loggedin, name='loggedin'),
     path('addbill/', views.getinput),
    path('logout/', views.logout_view, name='logout')
]