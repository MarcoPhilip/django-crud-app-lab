
from django.urls import path
from . import views

urlpatterns = [
   # Routes go here
   path('about/', views.about, name='about'),
   path('', views.home, name='home'),
   path('destinations', views.destination_index, name='destination_index')
]
