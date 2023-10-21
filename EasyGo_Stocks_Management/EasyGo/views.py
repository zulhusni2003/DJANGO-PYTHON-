# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from EasyGo.models import Staff
from EasyGo.models import Product
from EasyGo.models import FaQ
from EasyGo.models import Stock_management
from EasyGo.models import FaQ_management
 
def signin(request):
    return render (request,"signin.html")
 
def errorSignin(request):
    return render (request,"errorSignin.html")

def dashboard(request):
    if request.method == 'POST':
        staffID = request.POST.get('staffID')
        staffPassword = request.POST.get('staffPassword')
        
        try:
            user = Staff.objects.get(pk=staffID,staffID=staffID,staffPassword=staffPassword)
        except Staff.DoesNotExist:
            user = None 
        if user is not None:
            return render(request, 'dashboard.html', {})
        else:
            return redirect('errorSignin')
        
    return render(request, "dashboard.html")
  
def product(request):
    allproduct = Product.objects.all()
    dict={
        'allproduct': allproduct
    }
    return render (request,'product.html',dict)

def addProduct(request):
    if request.method == 'POST':
        s_ID = request.POST['staffID']
        p_ID = request.POST['productID']
        p_Name = request.POST['productName']
        p_price = request.POST['productPrice']
        p_Quantity = request.POST['productQuantity']
        p_expiration = request.POST['productExpirationDate']#YYYY-MM-DD 
        s_in = request.POST['stockIn']
        s_out = request.POST['stockOut']
        data1 = Product(productID = p_ID, productName = p_Name, productPrice = p_price, productQuantity = p_Quantity, productExpirationDate = p_expiration)
        data1.save()
        
        a = Staff.objects.get(staffID = s_ID)
        try:
            b = Product.objects.get(productID = p_ID)
        except Product.DoesNotExist:
            b = None 
        data2 = Stock_management(staffID=a, productID=b, stockIn=s_in, stockOut=s_out)
        data2.save()
        
    return render (request,"addProduct.html")
    
def stock(request):
    allstock = Stock_management.objects.all()
    dict={
        'allstock': allstock
    }
    return render (request,'stock.html',dict)

def productSection(request):
    product = Product.objects.all()
    dict={
        'product': product
    }
    return render (request,'productSection.html',dict)

def updateProduct(request,productID):
    data = Product.objects.get(productID=productID)
    dict = {
        'data':data
    }

    return render (request, "updateProduct.html",dict)

def save_update_product(request,productID):
    c_a = request.POST['productName']
    c_b = request.POST['productPrice']
    c_c = request.POST['productQuantity']
    c_d = request.POST['productExpirationDate']
    data = Product.objects.get(productID = productID)
    data.productName = c_a
    data.productPrice = c_b
    data.productQuantity = c_c
    data.productExpirationDate = c_d
    data.save()
    return HttpResponseRedirect(reverse('productSection'))

def productDeletePage(request):
    product = Product.objects.all()
    dict={
        'product': product
    }
    return render (request,"productDeletePage.html",dict)

def deleteProduct(request,productID):
        data2 = Product.objects.get(productID = productID)
        data2.delete()
        return HttpResponseRedirect(reverse('product'))

def faqtable(request):
    allfaq = FaQ_management.objects.all()
    dict={
        'allfaq': allfaq
    }
    return render (request,'faqtable.html',dict)

def faq(request):
    if request.method == 'POST':
        s_ID = request.POST['staffID']
        faq = request.POST['faqID']
        q = request.POST['question']
        data1 = FaQ(faqID = faq)
        data1.save()
         
        a = Staff.objects.get(staffID = s_ID)
        b = FaQ.objects.get(faqID = faq)
        data2 = FaQ_management(staffID=a, faqID=b, question=q)
        data2.save()
        
    return render (request,"faq.html")

def updatePassword(request):
    context = {"message": ""}
    if request.method == "POST":
        staffID = request.POST.get("staffID")
        staffPassword = request.POST.get("staffPassword")
        s_password_again = request.POST.get("s_password_again")

        staff = Staff.objects.filter(staffID=staffID)
        if staff.exists() and staffPassword == s_password_again:
            staff = staff.first()  # Get the first instance if it exists
            staff.staffPassword = s_password_again  # Update the staff's password
            staff.save()
            context = {
                "message": "Your password has been reset.",
                "message_type": "success",
            }
        else:
            context = {
                "message": "Error. Either you have not registered or both the entered passwords don't match.",
                "message_type": "error",
            }

    return render(request, "updatePassword.html", context)

def searchProduct(request): 
    if request.method == 'GET':
        data = Product.objects.filter(productID = request.GET.get('p_ID'))
        dict={
            'data': data
            }
        return render (request,'searchProduct.html',dict)
    else:
        return render (request,'searchProduct.html')
    
def staffTable(request):
    allStaff = Staff.objects.all()
    dict={
        'allStaff': allStaff
    }
    return render (request,'staffTable.html',dict)

def newStaff(request):
    if request.method == 'POST':
        s_ID = request.POST['staffID']
        s_n = request.POST['staffName']
        s_PN = request.POST['staffPhoneNumber']
        s_P = request.POST['staffPassword']
        data = Staff(staffID = s_ID, staffName = s_n, staffPhoneNumber = s_PN, staffPassword = s_P)
        data.save()
        
    return render (request,"newStaff.html")

def staffDeletePage(request):
    staff = Staff.objects.all()
    dict={
        'staff': staff
    }
    return render (request,"staffDeletePage.html",dict)

def deleteStaff(request,staffID):
        data = Staff.objects.get(staffID = staffID)
        data.delete()
        return HttpResponseRedirect(reverse('staffTable'))
    
def staffSection(request):
    staff = Staff.objects.all()
    dict={
        'staff': staff
    }
    return render (request,'staffSection.html',dict)

def updateStaff(request,staffID):
    data = Staff.objects.get(staffID=staffID)
    dict = {
        'data':data
    }

    return render (request, "updateStaff.html",dict)

def save_update_staff(request,staffID):
    c_a = request.POST['staffName']
    c_b = request.POST['staffPhoneNumber']
    data = Staff.objects.get(staffID = staffID)
    data.staffName = c_a
    data.staffPhoneNumber = c_b
    data.save()
    return HttpResponseRedirect(reverse('staffSection'))

def searchStaff(request): 
    if request.method == 'GET':
        data = Staff.objects.filter(staffID = request.GET.get('s_ID'))
        dict={
            'data': data
            }
        return render (request,'searchStaff.html',dict)
    else:
        return render (request,'searchStaff.html')
    


    




    
 
    









