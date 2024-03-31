from django.db import models

# Create your models here.

class Product(models.Model) :
    # sku = models.CharField(max_length = 255, primary_key = True)   if dont want django to automatically provide a id  attribute with primarty key option by default
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digit = 6, decimal = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)

class  Customer(models.Model) :
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.models.EmailField(max_length=254, unique = True)
    phone = models.IntegerField()
    birth_day = models.DateField(null = True)
