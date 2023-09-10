from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.fields import DecimalField
from tags.models import TaggedItem, ContentType
from store.models import Product


# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()
    list(query_set)
    query_set[0]
    return render(request, "hello.html", {"name": "Rami", "tags": list(query_set)})
