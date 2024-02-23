"""
URL configuration for medfi_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import signin
from patient import views as patient_view
from hospital import views as hospital_view

urlpatterns = [
    path("admin/", admin.site.urls),

    path("patient/profile/",patient_view.profile),
    path("patient/emergency",patient_view.emergency),
    path('signin', signin),
    path("patient/dashboard/",patient_view.index),
    path("hospital/dashboard/",hospital_view.index),
    path("hospital/doctors/",hospital_view.doctors),
    path("hospital/patient",hospital_view.upcoming_patient),
]
