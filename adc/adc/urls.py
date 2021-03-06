"""adc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from clinic.views import landing


urlpatterns = [
    path('', landing, name="landing"),
    path('admin/', admin.site.urls),
    path('clinic/',include('clinic.urls')),
    path('doctors/',include('doctors.urls')),
    path('patients/', include('patients.urls')), 
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = 'clinic.views.error_404'