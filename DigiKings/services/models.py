from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    Name = models.CharField(max_length=200,blank=True, null=True )
    email = models.CharField(max_length=200,blank=True, null=True )
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    

class ReferenceModel(models.Model):
    Name = models.CharField(max_length=200,blank=True, null=True )
    phone = models.CharField(max_length=200, blank=True, null=True)

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
    reference = models.ForeignKey(ReferenceModel, on_delete = models.CASCADE)


