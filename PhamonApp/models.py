from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=50)
    price=models.FloatField()
    discount=models.FloatField()
    description=models.CharField(max_length=100)
    size=models.CharField(max_length=10)
    brand= models.CharField(max_length=50)
    tyreimage=models.ImageField( upload_to='products')
    
    def __str__(self):
        return self.title
    
class ProductItem(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
    

class CartItem(models.Model):   
    name = models.ForeignKey('ProductItem', on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class Users(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)
    firstname=models.TextField(max_length=30)
    lastname= models.TextField(max_length=20)
    phoneNumber= models.CharField(max_length=14)
    address= models.TextField(max_length=20)
    
    def __str__(self):
        return self.email