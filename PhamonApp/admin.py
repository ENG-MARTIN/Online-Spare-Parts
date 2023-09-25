from django.contrib import admin
from .models import Product,ProductItem,Users
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductItem)

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','discount','description','size','brand','tyreimage']

class Products(admin.ModelAdmin):
    list_display=['name','size','price','brand','image']

class ApplicationUsers(admin.ModelAdmin):
    list_display=['email','password','firstname','lastname','phoneNumber','address'] 