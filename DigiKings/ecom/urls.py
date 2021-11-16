
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', home, name='home'),
  path('Ecom/Products',ProductView,name="ProductView"),
  path('Product-Detail/<str:slug>/<int:id>',Product_Detail,name="Product_Detail"),
  path('Ecom/filter-data/',filterData,name="filterData")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
