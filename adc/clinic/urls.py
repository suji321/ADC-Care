from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('patientregister/', views.patient_register.as_view(), name='patientregister'),
    path('doctorregister/', views.doctor_register.as_view(), name='doctorregister'),
    path('login/', views.login_request, name='login'),
    path('loggedin/', views.loggedin, name='loggedin'),   
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),   
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('404/', views.error, name='error'),
     path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
]