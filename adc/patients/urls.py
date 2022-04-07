from django.urls import path

from patients import views

urlpatterns = [
    path('patland/', views.patland,name='phome'),
    path('info/', views.patinfo, name='pat_info'),
    path('profileEdit/', views.profileEdit, name='pat_profile_edit'),
    path('medicalhistory/<str:pid>', views.patmedhis, name='pat_medhis'),
    path('bill/', views.patbill, name='pat_bill'),
    path('prescription/<str:pid>', views.prescription, name='pat_prescrip'),
    path('make-appt', views.createappt,name='pat_appointment')
]