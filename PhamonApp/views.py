from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
import json

from .models import Product,ProductItem,Users

# Create your views here.
def index(request):
    return render(request,"Home.html")

#----------------this loading the login form-----------------------------------
def Login(request):
        return render(request,"Login.html")
        
class TyreView(View):
    def get(self,request,val):
        return render( request, "Tyres.html", locals())
    
    
#----------------this is retrieving the items in the stock-----------------------------------
def Show(request):
    if 'size_' in request.GET:
        q=request.GET['size_']
        products=Product.objects.filter(size__icontains=q)
    else:
     products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,"Available.html",context)

#----------------this is the loading the  registration form-----------------------------------
def register_(request):
    return render(request,"RegistrationForm.html")

#-------------------------------------------------------------------------------
def cartgo(request):
    if 'size_' in request.GET:
        q=request.GET['size_']
        Products=ProductItem.objects.filter(size__icontains=q)
    else:
        Products=ProductItem.objects.all()
    context={
        'Products':Products
    }
    return render(request, 'Tyres.html', context)


##----------------this is the json function--------------------------------------

def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart = request.session.get('cart', [])
        cart.append(data)
        request.session['cart'] = cart
        request.session.save()
        return JsonResponse({'message': 'Item added to cart successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)


#----------------this is addding to cart-----------------------------------

def cart_contents(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart.html', {'cart': cart})

#----------------this is the login form-----------------------------------
def Loginform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(email=email, password=password)
        except Users.DoesNotExist:
            print("not found")
            user = None

        if user:
            return redirect('Home.html')

    return render(request, 'Login.html')