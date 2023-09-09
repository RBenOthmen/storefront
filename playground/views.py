from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


# Create your views here.
def say_hello(request):
    query_set = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    return render(request, "hello.html", {"name": "Rami", "orders": list(query_set)})
