from django.db import models

# Create your models here.
class Promotion (models.Model) :
    description  = models.CharField(max_length = 255)
    discount = models.FloatField()

class Product(models.Model) :
    # sku = models.CharField(max_length = 255, primary_key = True)   if dont want django to automatically provide a id  attribute with primarty key option by default
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digit = 6, decimal = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey('Collection', on_delete = models.PROTECT)
    promotions = models.ManyToManyField('Promotion')

class  Customer(models.Model) :
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    phone = models.IntegerField()
    birth_day = models.DateField(null = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.models.EmailField(max_length=254, unique = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)


class Order(models.Model) :
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETED, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS, default = PAYMENT_STATUS_PENDING)
    placed_at = models.DateTimeField(auto_now = True)
    customer = models.ForeignKey('Customer', on_delete = models.PROTECT)


class Address (models.Model) : 
    city = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    customer = models.OneToOneField('Customer' , on_delete = models.CASCADE, primary_key = True)

class Cart (models.Model) : 
    created_at = models.DateTimeField( auto_now_add=True)

class CartItem(models.Model) : 
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey('Cart', on_delete = models.CASCADE)
    product = models.ForeignKey("Product",on_delete=models.CASCADE)

class OrderItem (models.Model) : 
    order = models.ForeignKey("Order",  on_delete=models.PROTECT)
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Collection (models.Model) : 
    title = models.CharField(max_length = 255)
