from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db import transaction, connection
from django.db.models.functions import Concat
from django.db.models.fields import DecimalField
from tags.models import TaggedItem, ContentType
from store.models import Product, Collection, Order, OrderItem


# Create your views here.
def say_hello(request):
    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [1, 2, 'a'])
    query_set = Product.objects.raw('SELECT id, title FROM store_product')

    return render(request, "hello.html", {"name": "Rami"})
