from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Activity

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destination_index(request):
    destinations = Destination.objects.filter

    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })