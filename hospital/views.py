from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hospital/index.html")
def doctors(request):
    return render(request,"hospital/doctors.html")
def upcoming_patient(request):
    return render(request,"hospital/upcoming-patient.html")
def map(request):
    return render(request,"hospital/map.html")