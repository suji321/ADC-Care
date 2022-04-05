from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('patientregister/', views.patient_register.as_view(), name='patientregister'),
    path('doctorregister/', views.doctor_register.as_view(), name='doctorregister'),
    path('login/', views.login_request, name='login'),
    path('loggedin/', views.loggedin, name='loggedin'),   
    path('logout/', views.logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)