from django.shortcuts import render
from .models import Prensa

# Create your views here.

def prensa(request):

    prensa_items=Prensa.objects.all()
    return render(request,"prensa/prensa.html", {"prensa":prensa_items})
