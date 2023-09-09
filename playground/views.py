from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


# Create your views here.
def say_hello(request):
    query_set = OrderItem.objects.values("product_id").distinct()
    return render(request, "hello.html", {"name": "Rami", "products": list(query_set)})
