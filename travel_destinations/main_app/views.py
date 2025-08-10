from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Activity
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def destination_index(request):
    destinations = Destination.objects.all

    return render(request, 'destinations/index.html', {
        'destinations': destinations
    })

def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)

    return render(request, 'destinations/detail.html', {'destination': destination})


class DestinationCreate(CreateView):
    model = Destination
    fields = ['name', 'country', 'description']

class DestinationUpdate(UpdateView):
    model = Destination
    fields = ['name', 'country', 'description']

class DestinationDelete(DeleteView):
    model = Destination
    success_url = '/destinations/'
