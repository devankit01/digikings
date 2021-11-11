from django.shortcuts import render
from .models import *
# Create your views here.


def AddNew(request):
    if request.method == 'POST':
        # Customer
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        customer_address = request.POST.get('customer_address')
        print(customer_name, customer_phone, customer_email, customer_address)
        customer_obj = CustomerModel(Name=customer_name, email=customer_email,
                            phone=customer_phone, address=customer_address)
        customer_obj.save()

        # Reference
        reference_name = request.POST.get('reference_name')
        reference_phone = request.POST.get('reference_phone')
        print(reference_name, reference_phone)
        reference_obj = ReferenceModel(
            Name=reference_name, phone=reference_phone)
        reference_obj.save()

        # Product
        product_brand = request.POST.get('product_brand')
        product_type = request.POST.get('product_type')
        product_category = request.POST.get('product_category')
        submit_date = request.POST.get('submit_date')
        submit_month = request.POST.get('submit_month')
        submit_year = request.POST.get('submit_year')
        print(product_brand, product_type, product_category,
              submit_date, submit_month, submit_year)

        total_amount = request.POST.get('total_amount')
        paid_amount = request.POST.get('paid_amount')
        pending_amount = request.POST.get('pending_amount')
        problem = request.POST.get('problem')

        return_date = request.POST.get('return_date')
        return_month = request.POST.get('return_month')
        return_year = request.POST.get('return_year')

        print(total_amount, paid_amount, pending_amount,
              problem, return_date, return_month, return_year)

        if request.POST.get('is_Paid'):
            is_Paid = True
        else:
            is_Paid = False
        print(is_Paid)

        # Unique Key
        import uuid

        # Printing random id using uuid1()

        s = str(uuid.uuid1())
        print(s[0:8])

        service_obj = ServiceModel(id=s[0:8], Brand=product_brand, DesktopType=product_type,
            DesktopCategory=product_category, Problem=problem,
            Submit_date=submit_date, Submit_month=submit_month,
            Submit_year=submit_year, total_amount=total_amount, paid_amount=paid_amount,
            residual_amount=pending_amount, is_fullyPaid=is_Paid,
            return_date=return_date, return_month=return_month, return_year=return_year,
            customer=customer_obj, reference=reference_obj)
        service_obj.save()

        return render(request, 'services/addNewService.html')

    return render(request, 'services/addNewService.html')


def AllServices(request):
    services = ServiceModel.objects.all()[::-1]
    return render(request, 'services/AllService.html', {'services': services})


def EditService(request, id):
    i = ServiceModel.objects.get(id=id)

    if request.method == 'POST': 

        i.customer.Name = request.POST.get('customer_name')
        i.customer.phone = request.POST.get('customer_phone')
        i.customer.email = request.POST.get('customer_email')
        i.customer.address = request.POST.get('customer_address')
        i.customer.save()

        i.reference.Name = request.POST.get('reference_name')
        i.reference.phone = request.POST.get('reference_phone')
        i.reference.save()

        i.Brand = request.POST.get('product_brand')
        i.DesktopType = request.POST.get('product_type')
        i.DesktopCategory = request.POST.get('product_category')
        i.Submit_date = request.POST.get('submit_date')
        i.Submit_month = request.POST.get('submit_month')
        i.Submit_year = request.POST.get('submit_year')


        i.total_amount = request.POST.get('total_amount')
        i.paid_amount = request.POST.get('paid_amount')
        i.residual_amount = request.POST.get('pending_amount')
        i.Problem = request.POST.get('problem')

        i.return_date = request.POST.get('return_date')
        i.return_month = request.POST.get('return_month')
        i.return_year = request.POST.get('return_year')

        if request.POST.get('is_Paid'):
            i.is_fullyPaid = True
        else:
            i.is_fullyPaid = False


        i.save()

        return render(request, 'services/EditService.html', {'i': i})
    return render(request, 'services/EditService.html', {'i': i})
