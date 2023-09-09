from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer
from django.db.models.fields import DecimalField


# Create your views here.
def say_hello(request):
    discounted_price = ExpressionWrapper (
        F('unit_price') * 0.8, output_field=DecimalField())
    query_set = Product.objects.annotate(discounted_price=discounted_price)
    return render(request, "hello.html", {"name": "Rami", "result": list(query_set)})