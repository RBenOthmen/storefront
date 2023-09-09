from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Product, OrderItem, Order, Customer


# Create your views here.
def say_hello(request):
    query_set = Customer.objects.annotate(new_id=F("id") + 1)
    return render(request, "hello.html", {"name": "Rami", "result": list(query_set)})
