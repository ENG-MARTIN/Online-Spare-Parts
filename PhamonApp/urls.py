from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.index ),
    #path('admins/',views.loadAdministrator),
    #path('tyre/<slug:val>',views.TyreView.as_view(), name="tyres"),
    path('login/',views.Login, name="login"),
    path('Tyres/',views.Show, name="showtyres"),
    path('registration/',views.register_, name="registration"),
    path('cartgo/',views.cartgo, name="cartgo"),
    path('cartgo/cart_view/',views.cart_contents,name='cart_view'),
    path('cart_view/',views.cart_contents,name='cart_view'),
    
    #calling the json function
     path('cartgo/add_to_cart/',views.cart_contents, name='add_to_cart'),
     
    path('logging/',views.Loginform,name='loginform'),
]
admin.site.index_title="Phamon Admin"
#admin.site.site_title="Phamon Admin"
