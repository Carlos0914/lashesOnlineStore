from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def catalog(request):
    return render(request, "catalog.html", {})

def schedule(request):
    return render(request, "schedule.html", {})

def location(request):
    return render(request, "location.html", {})
