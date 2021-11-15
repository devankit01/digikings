from django.db import models
from ecom.models import Product
# Create your models here.

class CustomerModel(models.Model):
    Name = models.CharField(max_length=200,blank=True, null=True )
    email = models.CharField(max_length=200,blank=True, null=True )
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    

# class ReferenceModel(models.Model):
#     Name = models.CharField(max_length=200,blank=True, null=True )
#     phone = models.CharField(max_length=200, blank=True, null=True)
class RetailerModel(models.Model):
    ID = models.CharField(max_length=200,primary_key=True)
    Name = models.CharField(max_length=200,blank=True, null=True )
    Phone = models.IntegerField(null=True)
    Email = models.CharField(max_length=200, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)

class ServiceModel(models.Model):
    id = models.CharField(max_length=10, primary_key = True)
    Brand = models.CharField(max_length=200, blank=True, null=True)
    DesktopType = models.CharField(max_length=200, blank=True, null=True) # Assembled, Branded Choices
    DesktopCategory = models.CharField(max_length=200, blank=True, null=True) # Laptop, Desktop Choices
    Problem = models.TextField(blank=True, null=True)

    Submit_date = models.CharField(max_length=100, blank=True, null=True)
    Submit_month = models.CharField(max_length=100, blank=True, null=True)
    Submit_year = models.CharField(max_length=100, blank=True, null=True)

    return_date = models.CharField(max_length=100, blank=True, null=True)
    return_month = models.CharField(max_length=100, blank=True, null=True)
    return_year = models.CharField(max_length=100, blank=True, null=True)

    total_amount = models.IntegerField( blank=True, null=True)
    paid_amount = models.IntegerField( blank=True, null=True)
    residual_amount = models.IntegerField( blank=True, null=True)
    is_fullyPaid = models.BooleanField(default=False, blank=True, null=True)

    customer = models.ForeignKey(CustomerModel, on_delete = models.CASCADE)
    reference = models.ForeignKey(RetailerModel, on_delete = models.CASCADE)


# Team Members

class TeamModel(models.Model):
    ID = models.CharField(max_length=200,primary_key=True)
    Name = models.CharField(max_length=200,blank=True, null=True )
    Phone = models.IntegerField(null=True)
    Email = models.CharField(max_length=200, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    ProfilePic = models.ImageField(upload_to = 'profile/')
    Salary = models.CharField( max_length =10 , blank=True, null=True, default = "Variable Salary")
    Post = models.CharField(max_length=200, blank=True, null=True)



# Offline Shop Sales
class OfflineShopSale(models.Model):
    CustomerName = models.CharField(max_length=200, null=True, blank=True)
    CustomerPhone = models.CharField(max_length=200, null=True, blank=True)
    CustomerEmail = models.CharField(max_length=200, null=True, blank=True)
    TotalAmount = models.IntegerField(default = 0, null=True, blank=True)
    PaidAmount = models.IntegerField(default = 0, null=True, blank=True)
    DueAmount = models.IntegerField(default = 0, null=True, blank=True)
    isPaid = models.BooleanField(default = False)
    SaleDate = models.DateField(null=True, blank=True) 
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)


# <tr><td>Date of Birth</td><td><input type="date" name="DOB" value="{{m.dob|date:"d/m/Y"}}" required=True></td></tr>

# value="{{m.dob|date:'d/m/Y'}}" which must be specified as value="{{m.dob|date:'Y-m-d'}}"