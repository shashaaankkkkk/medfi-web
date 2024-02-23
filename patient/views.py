from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request , "patient/patient-profile.html")
def index(request):
    return render(request,"patient/index.html")
def emergency(request):
    return render(request,"patient/emergency.html")