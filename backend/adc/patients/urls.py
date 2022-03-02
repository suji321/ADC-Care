from django.urls import path
from patients import views

urlpatterns = [
    path('patland/', views.patland),
    path('info/<str:pid>', views.patinfo, name='info'),
    path('medicalhistory/<str:pid>', views.patmedhis, name='medhis'),
    path('bill/<str:pid>', views.patbill, name='bill'),
    path('prescription/<str:pid>', views.prescription, name='prescrip')
]