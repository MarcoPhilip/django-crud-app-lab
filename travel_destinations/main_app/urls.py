
from django.urls import path
from . import views

urlpatterns = [
   # Routes go here
   path('about/', views.about, name='about'),
   path('', views.home, name='home'),
   path('destinations/', views.destination_index, name='destinations'),
   path('destinations/<int:destination_id>/', views.destination_detail, name='destination-detail'),
   path('destinations/create/', views.DestinationCreate.as_view(), name='destination-create'),
   path('destinations/<int:pk>/update', views.DestinationUpdate.as_view(), name='destination-update'),
   path('destinations/<int:pk>/delete', views.DestinationDelete.as_view(), name='destination-delete'),
]
