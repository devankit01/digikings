from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Item_Quality)
class ProductAdmin(admin.ModelAdmin):
    list_display=('ProductName','Price_Product','Item_quality','image_tag')

admin.site.register(Product,ProductAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customers','Product_id','Status')

admin.site.register(Orders,OrderAdmin)