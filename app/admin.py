from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from django.contrib import admin
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced,
)
@admin.register(Customer)
class CustomerModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discounted_price','brand','product_image','description','Category',]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status']


def customer_info(self, obj):
    link = reverse("admin:app:app_customer_change", args=[obj.customer.pk])
    return format_html('<a href="{}">{}</a>',link,obj.customer.name)
