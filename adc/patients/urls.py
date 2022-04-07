from django.urls import path

from patients import views

urlpatterns = [
    path('patland/', views.patland,name='phome'),
    path('info/', views.patinfo, name='info'),
    path('profileEdit/', views.profileEdit, name='profileEdit'),
    path('medicalhistory/<str:pid>', views.patmedhis, name='medhis'),
    path('bill/<str:pid>', views.patbill, name='bill'),
    path('prescription/<str:pid>', views.prescription, name='prescrip'),
    path('make-appt', views.createappt,name='appointment')
]