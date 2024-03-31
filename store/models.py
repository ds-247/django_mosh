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
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    email = models.models.EmailField(max_length=254, unique = True)
    phone = models.IntegerField()
    birth_day = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)


class Orders(models.Model) :
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