from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.fields import DecimalField
from tags.models import TaggedItem, ContentType
from store.models import Product, Collection


# Create your views here.
def say_hello(request):
    collection = Collection(pk=11)
    collection.delete()

    Collection.objects.filter(id__lt=5).delete()

    return render(request, "hello.html", {"name": "Rami"})
