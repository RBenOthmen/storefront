from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer


# Create your views here.
def say_hello(request):
    query_set = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, "hello.html", {"name": "Rami", "result": list(query_set)})
