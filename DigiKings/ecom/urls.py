
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', home, name='home'),
  path('Ecom/Products',ProductView,name="ProductView"),
  path('Product-Detail/<str:slug>/<int:id>',Product_Detail,name="Product_Detail"),
  path('Ecom/filter-data/',filterData,name="filterData"),
  path('Add-to-cart/',add_to_cart,name="add_to_cart"),
  path('Cart-Details/',Cart_View,name="Cart_View"),
  path('Delete-Cart-item/',Delete_Cart_item,name="Delete_Cart_item"),
  path('Update-Cart-item/',Update_cart_items,name="Update_cart_items"),
  path('Cart-Details/<str:user>/checkout/',CheckOut,name="CheckOut"),
  path('reviewed-save/<int:pid>/',Save_Review,name="Save_Review"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
