from django.db import models

# Create your models here.
from user.models import Profile
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Brand(models.Model):
    Brand_Title=models.CharField(max_length=200,null=True)
    Brand_logo=models.ImageField(upload_to='Orders/Images')
    def __str__(self):
        return self.Brand_Title

class Categories(models.Model):
    categories=models.CharField(max_length=200,null=True)
    class Meta:
        verbose_name_plural='1. Categories'
    def __str__(self):
        return str(self.categories)

class Item_Quality(models.Model):
    item_qualities=(
        ("First Hand","First Hand"),
        ("Second Hand","Second Hand"),
    )
    Item_quality=models.CharField(choices=item_qualities,max_length=100,null=True)
    def __str__(self):
        return self.Item_quality

class Product(models.Model):
    item_quality=(
        ("First Hand","First Hand"),
        ("Second Hand","Second Hand"),
    )
    
    ProductName=models.CharField(max_length=200,null=True)
    slug=models.SlugField(max_length = 250, null = True, blank = True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    Product_Image=models.ImageField(upload_to='Product/Images', blank=True)
    Price_Product=models.PositiveIntegerField(null=True)
    Brand_name=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    Item_quality=models.ForeignKey(Item_Quality,on_delete=models.CASCADE,null=True)
    Description=models.TextField(null=True)
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/> ' % (self.Product_Image.url))
    def __str__(self):
        return str(self.ProductName)

class Orders(models.Model):
    choices=(
        ("ordered","ordered"),
        ("order_confirmed","order_confirmed"),
        ("out for delivery","out for delivery"),
        ("Order Recieved","Order Recieved"),
        ("Order Reject","Order Reject"),
    )
    customers=models.ForeignKey(Profile,on_delete=models.CASCADE)
    Product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Status=models.CharField(max_length=200,choices=choices)
    quantity=models.IntegerField( max_length=5)

    def __str__(self):
        return self.Product_id.ProductName

