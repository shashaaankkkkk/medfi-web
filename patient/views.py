from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request , "patient/profile.html")
def index(request):
    return render(request,"patient/index.html")