from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hospital/index.html")
def doctors(request):
    return render(request,"hospital/doctors.html")