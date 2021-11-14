
from django import urls
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
  path('add_service', AddNew, name = 'AddNew'),
  path('all_services', AllServices, name = 'AllServices'), 
  path('edit_service/<id>', EditService, name = 'EditService'),

  path('add_retailer', AddRetailer, name = 'AddRetailer'),
  path('all_retailer', AllRetailer, name = 'AllRetailer'),
  path('edit_retailer/<id>', EditRetailer, name = 'EditRetailer'),

    path('add_team', AddTeam, name = 'AddTeam'),
  path('all_team', AllTeam, name = 'AllTeam'), 
  path('edit_team/<id>', EditTeam, name = 'EditTeam'),



]
