
from django import urls
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
  path('add-new-service', AddNew, name = 'AddNew'),
  path('all-services', AllServices, name = 'AllServices'), 
  path('edit-service/<id>', EditService, name = 'EditService')
]
