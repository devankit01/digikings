from django.shortcuts import render,get_object_or_404,HttpResponse
from . models import Categories, Item_Quality, Product,Orders,CartOrderItems
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Min, Max
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home/index.html')


def ProductView(request):
   
    try:
        products=Product.objects.all().order_by('-id')
        categories=Product.objects.distinct().values('category__categories','category__id')
        Brand=Product.objects.distinct().values('Brand_name__Brand_Title','Brand_name__id')
        Item_quality=Product.objects.distinct().values('Item_quality__Item_quality','Item_quality__id')
        price=Product.objects.values('Price_Product')
        minMaxPrice=Product.objects.aggregate(Min('Price_Product'),Max('Price_Product'))
        
     
    except:
        products=[]
        categories=[]
        Brand=[]
        Item_quality=[]
        price=[]
        minMaxPrice=[]

    return render(request,'ecom/products.html',{'products':products,'Categroies':categories,'Brand':Brand,'itemsQ':Item_quality,'price':price,'minMaxPrice':minMaxPrice})


def category_product_list(request,cat_id):
    categoryies=Categories.objects.get(id=cat_id)
    products=Product.objects.filter(category=categoryies).order_by('-id')
    return render(request,'ecom/products.html',{'products':products})


# Product Detail
def Product_Detail(request,slug,id):
    product=Product.objects.get(id=id)
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:3]
    canAdd=True
    user = get_object_or_404(User, username=request.user)
    users = get_object_or_404(Profile, username=user)
    reviewCheck=ProductReviewed.objects.filter(user=users,Product=product).count()
    if request.user.is_authenticated:
        if reviewCheck>0:
            canAdd=False

    reviews=ProductReviewed.objects.filter(Product=product)
    # print(reviews.review_text)
    return render(request,'ecom/product_detail.html',{'data':product,'related_product':related_products,'ReviewAdd':canAdd,'reviews':reviews})


def filterData(request):
    categories=request.GET.getlist('categories[]')
    itemQuality=request.GET.getlist('Item_quality[]')
    BrandName=request.GET.getlist('Brand_name[]')
    minPrice=request.GET.get('_minPrice')
    maxPrice=request.GET.get('_maxPrice')
    allProduct=Product.objects.all().order_by('-id').distinct()
    # print("aaya")
    allProduct=allProduct.filter(Price_Product__gte=minPrice)
    allProduct=allProduct.filter(Price_Product__lte=maxPrice)
    if len(categories)>0:
        allProduct=allProduct.filter(category__id__in=categories).distinct()
    # if len(priceProduct)>0:
    #     allProduct=allProduct.filter(Price_Product__in=priceProduct).distinct()
    if len(itemQuality)>0:
        allProduct=allProduct.filter(Item_quality__id__in=itemQuality).distinct()
    if len(BrandName)>0:
        allProduct=allProduct.filter(Brand_name__id__in=BrandName).distinct()
    t=render_to_string('ecom/ajax_product_list.html',{'products':allProduct})
    
    return JsonResponse({'products':t})


def add_to_cart(request):
    # del request.session['cartdata']
    cart_p={}
    cart_p[str(request.GET['id'])]={
        'title':request.GET['title'],
        'qty':request.GET['qty'],
        'Price':request.GET['Price'],
        'image':request.GET['image']
    }


    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata']=cart_data
        else:
            cart_data=request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata']=cart_data
    else:
        request.session['cartdata']=cart_p
    return JsonResponse ({'data':request.session['cartdata'],'totaItems':len(request.session['cartdata'])})


def Cart_View(request):
    total_amount=0
    for p_id,items in request.session['cartdata'].items():
        total_amount+=int(items['qty'])*float(items['Price'])

    return render(request,'ecom/cart.html',{'cart_data':request.session['cartdata'],'totaItems':len(request.session['cartdata']),'total_amt':total_amount})

# Delete Cart items 
def Delete_Cart_item(request):
    p_id=request.GET['id']
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            del request.session['cartdata'][p_id]
            request.session['cartdata']=cart_data
    total_amount=0
    for p_id,items in request.session['cartdata'].items():
        total_amount+=int(items['qty'])*float(items['Price'])
    t=render_to_string('ecom/ajax_cart_list.html',{'cart_data':request.session['cartdata'],'totaItems':len(request.session['cartdata']),'total_amt':total_amount})
    
    return JsonResponse({'data':t,'totaItems':len(request.session['cartdata'])})
# update cart items 
def Update_cart_items(request):
    p_id=request.GET['id']
    p_qty=request.GET['qty']
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty']=p_qty
            request.session['cartdata']=cart_data
    total_amount=0
    for p_id,items in request.session['cartdata'].items():
        total_amount+=int(items['qty'])*float(items['Price'])
    t=render_to_string('ecom/ajax_cart_list.html',{'cart_data':request.session['cartdata'],'totaItems':len(request.session['cartdata']),'total_amt':total_amount})
    
    return JsonResponse({'data':t,'totaItems':len(request.session['cartdata'])})


def CheckOut(request,user):
    total_amt=0
    TotalAmt=0
    # if 'cartdata' in request.session:
    #     # orders 
    #     for p_id,items in request.session['cartdata'].items():
    #         TotalAmt+=int(items['qty'])*float(items['Price'])
    #     user = get_object_or_404(User, username=request.user)
    #     users = get_object_or_404(Profile, username=user)
    #     order=Orders.objects.create(
    #         customers=users,
    #         total_amount=TotalAmt,
           
    #     )
    #     # end 
    #     # order Items
    #     for p_id,items in request.session['cartdata'].items():
    #         total_amt+=int(items['qty'])*float(items['Price'])
    #         items=CartOrderItems.objects.create(
    #             order=order,
    #             invoice_No='INV-'+str(order.id),
    #             item=items['title'],
    #             quantity=items['qty'],
    #             Image=items['image'],
    #             Price=items['Price'],
    #             Total=float(items['qty'])*float(items['Price'])
    #         )
    # **************for checking login***************
    try:
        user = get_object_or_404(User, username=request.user)
        user = get_object_or_404(Profile, username=user)
        if user:
            return render(request,'ecom/Order_delivery.html')
    except:
        return redirect('signin')


def Save_Review(request,pid):
    print(pid)
    rew_txt=request.POST['message']
    print(request.POST['ratings'])
    product=Product.objects.get(id=pid)
    user = get_object_or_404(User, username=request.user)
    users = get_object_or_404(Profile, username=user)
    review=ProductReviewed.objects.create(user=users,Product=product,review_text=rew_txt,review_rating=request.POST['ratings'])
    data={
        'review_text':request.POST['message'],
        'first_name':user.first_name,
        'last_name':user.last_name,
        'review_rating':int(request.POST['ratings'])
    }
    return JsonResponse({"data":data})