
from django import urls
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecom.urls')),
    path('services/', include('services.urls')),
    path('accounts/', include('user.urls')),

]
