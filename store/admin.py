import django.db.models
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request: Any, model_admin: Any):
        return [("<10", "Low")]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 10
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "placed_at", "customer")
    list_per_page = 10
    list_select_related = ["customer"]

    def customer_id(self, order):
        return order.customer_id


# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ["title", "products_count"]

#     @admin.display(ordering="products_count")
#     def products_count(self, collection):
#         url = (
#             reverse("admin:store_product_changelist")
#             + "?"
#             + urlencode({"collection__id": str(collection.id)})
#         )
#         return format_html(
#             '<a href="http://google.com">{}</a>', collection.products_count
#         )

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 10
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]


admin.site.register(models.Collection)
