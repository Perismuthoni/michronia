from django.http.response import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . inherit import cartData
from django.core import serializers
from .forms import ContactForm

def index(request):
    return render(request, "webfiles/home/home.html",)

def home(request):
    return render(request, "webfiles/home/home.html",)

def services(request):
    return render(request, "webfiles/services/services.html",)
def keeping(request):
    return render(request, "webfiles/services/keeping.html",)
def consultancy(request):
    return render(request, "webfiles/services/consultancy.html",)

def Accountancy(request):
    return render(request, "webfiles/services/Accountancy.html",)
def Advisory(request):
    return render(request, "webfiles/services/Advisory.html",)

def about(request):
    return render(request, "webfiles/about_us/about_us.html",)

def contact(request):
    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        alert = True
        return render(request, 'webfiles/contact_us/contact.html', {'alert':alert})
    return render(request, "webfiles/contact_us/contact.html")

# def contact(request):
#     	if request.method == "POST":
#          form = ContactForm(request.POST)
#          if form.is_valid():
#              subject = "Website Inquiry"
#              body = {
# 			'full_name': form.cleaned_data['full_name'],
#             'email_address': form.cleaned_data['email_address'],
#             'phone_number': form.cleaned_data['phone_number'],
# 			'service': form.cleaned_data['last_name'],			 
# 			'message':form.cleaned_data['message'], 
# 			}
#              message = "\n".join(body.values())
                         
#              try:
#                   send_mail(subject, message, 'muthonimuriuki22@gmail.com', ['muthonimuriuki22@gmail.com'])
#              except BadHeaderError:
#                   return HttpResponse('Invalid header found.')
#              return redirect ("webfiles/home/home.html")
         
#          form = ContactForm()
#          return render(request, "webfiles/contact_us/contact.html", {'form':form})
                                        
			    
        
		
				
			
      
	
	


















def search(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    if request.method == "POST":
        search = request.POST['search']
        products = Product.objects.filter(name__contains=search)
        return render(request, "search.html", {'search':search, 'products':products, 'cartItems':cartItems})
    else:
        return render(request, "search.html")


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "webfiles/auth/change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "webfiles/auth/change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "webfiles/auth/change_password.html", {'cartItems':cartItems})



def loggedin_contact(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    if request.method=="POST":       
        name = request.user
        email = request.user.email
        phone = request.user.customer.phone_number
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        alert = True
        return render(request, 'webfiles/auth/loggedin_contact.html', {'alert':alert})
    return render(request, "webfiles/auth/loggedin_contact.html", {'cartItems':cartItems})



def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            full_name=request.POST['full_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone_number = request.POST['phone_number']
            email = request.POST['email']

            if password1 != password2:
                alert = True
                return render(request, "webfiles/auth/register.html", {'alert':alert})
            
            user = User.objects.create_user(username=username, password=password1, email=email)
            customers = Customer.objects.create(user=user, name=full_name, phone_number=phone_number, email=email)
            user.save()
            customers.save()
            return render(request, "webfiles/auth/login.html")
    return render(request, "webfiles/auth/register.html")
    
def registerbsn(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            bsn_name = request.POST['bsn_name']
            full_name=request.POST['full_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            owner_email = request.POST['owner_email']
            bsn_location = request.POST['bsn_location']
            bsn_type = request.POST['bsn_type']

            if password1 != password2:
                alert = True
                return render(request, "webfiles/auth/registerbsn.html", {'alert':alert})
            
            user = User.objects.create_user(username=username, password=password1, email=email )
            customers = Customer.objects.create(user=user, name=full_name, phone_number=phone_number, email=email)
            business = Business.objects.create(user=user, name=bsn_name, phone_number=phone_number,bsn_location= bsn_location,bsn_type=bsn_type,  email=email,owner_email =owner_email,owner=full_name,)
            user.save()
            customers.save()
            business.save()
            return render(request, "webfiles/auth/login.html")
    return render(request, "webfiles/auth/registerbsn.html")


def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                alert = True
                return render(request, "webfiles/auth/login.html", {"alert":alert})
    return render(request, "webfiles/auth/login.html")

def Logout(request):
    logout(request)
    alert = True
    return render(request, "index.html", {'alert':alert})

# def analytics(request):
#     return render(request, 'analytics.html', {})

# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)