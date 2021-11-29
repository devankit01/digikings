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
    list_display=('customers','Status','order_dt','total_amount','paid_status')
admin.site.register(Orders,OrderAdmin)

class CartOrderItem(admin.ModelAdmin):
    list_display=('order','invoice_No','item','quantity','image_tag','Price','Total')

admin.site.register(CartOrderItems,CartOrderItem)

class ProductReview(admin.ModelAdmin):
    list_display=('user','Product','review_rating','Product')

admin.site.register(ProductReviewed,ProductReview)