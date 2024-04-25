from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem, Collection, Promotion, Customer, Order
from django.db.models import F, Value
from django.db.models.functions import Concat


# Create your views here.

def  say_hello(request) : 
    # query_set = Product.objects.all();
    # query_set = Product.objects.filter(id__in = Collection.objects.values('id'));  check query
    # query_set = Collection.objects.all()
    # query_set = Product.objects.filter(collection__title = 'Beauty')
    # query_set = Product.objects.prefetch_related('promotions')
    # query_set = Product.objects.values("title", "promotions__description")
    # query_set = Promotion.objects.all()
    # query_set = Product.objects.select_related('collection')
    # query_set = Customer.objects.annotate(full_name = Concat('first_name', Value(" "), 'last_name'));

    query_set = Order.objects.order_by('-placed_at').select_related('customer').prefetch_related('orderitem_set__product')[:5];
    
    return render(request, 'hello.html', {'name' : 'Dipanshu', 'products' : list(query_set)})
