from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from user.views import Error404
# Create your views here.


def AddNew(request):
    if checkSuperUser(request):

        retail = RetailerModel.objects.all()

        if request.method == 'POST':
            # Customer
            customer_name = request.POST.get('customer_name')
            customer_phone = request.POST.get('customer_phone')
            customer_email = request.POST.get('customer_email')
            customer_address = request.POST.get('customer_address')
            print(customer_name, customer_phone,
                  customer_email, customer_address)
            customer_obj = CustomerModel(Name=customer_name, email=customer_email,
                                         phone=customer_phone, address=customer_address)
            customer_obj.save()

            # Reference

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
            retailer = request.POST.get('retailer')
            retail_obj = RetailerModel.objects.get(Name=retailer)

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
                                       customer=customer_obj, reference=retail_obj)
            service_obj.save()

            return render(request, 'services/addNewService.html', {'retail': retail})

        return render(request, 'services/addNewService.html', {'retail': retail})
    else:
        return redirect('Error404')


def AllServices(request):
    if checkSuperUser(request):
        services = ServiceModel.objects.all()[::-1]
        return render(request, 'services/AllService.html', {'services': services})
    else:
        return redirect('Error404')


def EditService(request, id):
    if checkSuperUser(request):

        retail = RetailerModel.objects.all()

        i = ServiceModel.objects.get(id=id)

        if request.method == 'POST':

            i.customer.Name = request.POST.get('customer_name')
            i.customer.phone = request.POST.get('customer_phone')
            i.customer.email = request.POST.get('customer_email')
            i.customer.address = request.POST.get('customer_address')
            i.customer.save()

            retailer = request.POST.get('retailer')
            print("Retailer : ", retailer)
            retail_obj = RetailerModel.objects.get(Name=retailer)
            i.reference = retail_obj

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

            return redirect('AllServices')
        return render(request, 'services/EditService.html', {'i': i, 'retail': retail})
    else:
        return redirect('Error404')

# Retailer


def AddRetailer(request):
    if checkSuperUser(request):

        retail = RetailerModel.objects.all()
        if request.method == 'POST':
            retailer_name = request.POST.get('retailer_name')
            retailer_phone = request.POST.get('retailer_phone')
            retailer_email = request.POST.get('retailer_email')
            retailer_address = request.POST.get('retailer_address')
            count = len(retail)

            id = 'DIGIRETAILER-' + str(int(count+101))

            obj = RetailerModel(ID=id, Name=retailer_name,
                                Email=retailer_email, Phone=retailer_phone, Address=retailer_address)
            obj.save()
            return redirect('AllRetailer')

        return render(request, 'services/addNewRetailer.html')
    else:
        return redirect('Error404')


def AllRetailer(request):
    if checkSuperUser(request):

        retail = RetailerModel.objects.all()
        return render(request, 'services/AllRetailers.html', {'retail': retail})
    else:
        return redirect('Error404')


def EditRetailer(request, id):
    if checkSuperUser(request):

        i = RetailerModel.objects.get(ID=id)
        if request.method == 'POST':
            i.Name = request.POST.get('retailer_name')
            i.Email = request.POST.get('retailer_email')
            i.Phone = request.POST.get('retailer_phone')
            i.Address = request.POST.get('retailer_address')
            i.save()
            return redirect('AllRetailer')
        return render(request, 'services/EditRetailer.html', {'i': i})
    else:
        return redirect('Error404')


def AddTeam(request):
    if checkSuperUser(request):

        retail = TeamModel.objects.all()
        if request.method == 'POST':
            member_name = request.POST.get('member_name')
            member_phone = request.POST.get('member_phone')
            member_email = request.POST.get('member_email')
            member_address = request.POST.get('member_address')
            member_salary = request.POST.get('member_salary')
            member_post = request.POST.get('member_post')
            member_pic = request.FILES.get('member_pic')
            count = len(retail)

            id = 'DIGIEMP-' + str(int(count+101))
            print(id, member_name, member_phone, member_email,
                  member_address, member_salary, member_post, member_pic)

            obj = TeamModel(ID=id, Name=member_name,
                            Email=member_email, Phone=member_phone, Address=member_address, Salary=member_salary, Post=member_post, ProfilePic=member_pic)
            obj.save()
            return redirect('AllTeam')
        return render(request, 'services/addNewTeam.html')
    else:
        return redirect('Error404')


def AllTeam(request):
    if checkSuperUser(request):
        team = TeamModel.objects.all()
        return render(request, 'services/AllTeam.html', {'team': team})
    else:
        return redirect('Error404')


def EditTeam(request, id):
    if checkSuperUser(request):
        i = TeamModel.objects.get(ID=id)
        if request.method == 'POST':
            i.Name = request.POST.get('member_name')
            i.Phone = request.POST.get('member_phone')
            i.Email = request.POST.get('member_email')
            i.Address = request.POST.get('member_address')
            i.Salary = request.POST.get('member_salary')
            i.Post = request.POST.get('member_post')
            i.ProfilePic = request.FILES.get('member_pic')
            i.save()
            return redirect('AllTeam')
        return render(request, 'services/EditTeam.html', {'i': i})
    else:
        return redirect('Error404')


def checkSuperUser(request):
    if request.session.has_key('username'):
        uid = User.objects.get(username=request.session['username'])
        # USER is SuperUser
        print(uid.is_superuser)
        if uid.is_superuser:
            return True
    else:
        print('No Login')
        return False
