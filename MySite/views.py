from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request,"MySite/home.html")

def bio(request):
    return render(request,"MySite/bio.html")

def escuela(request):
    return render(request,"MySite/escuela.html")


