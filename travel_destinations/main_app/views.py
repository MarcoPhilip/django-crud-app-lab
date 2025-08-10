from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination, Activity
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ActivityForm
from django.urls import reverse

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
    activity_form = ActivityForm()
    return render(request, 'destinations/detail.html',{
        'destination': destination,
        'activity_form': activity_form
    })

def add_activity(request, destination_id):
    form = ActivityForm(request.POST)

    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.destination_id = destination_id
        new_activity.save()
    return redirect('destination-detail', destination_id=destination_id)

class DestinationCreate(CreateView):
    model = Destination
    fields = ['name', 'country', 'description']

class DestinationUpdate(UpdateView):
    model = Destination
    fields = ['name', 'country', 'description']

class DestinationDelete(DeleteView):
    model = Destination
    success_url = '/destinations/'

class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['name', 'description']

    def get_success_url(self):
        destination_id = self.object.destination.id
        
        return reverse(
            'destination-detail',
            kwargs={'destination_id': destination_id}
        )

class ActivityDelete(DeleteView):
    model = Activity
    
    def get_success_url(self):
        destination_id = self.object.destination.id
        
        return reverse(
            'destination-detail',
            kwargs={'destination_id': destination_id}
        )