from django.contrib import admin
from .models import Orders, Products, ProductsInOrders


# admin.site.register(Orders)
# admin.site.register(Products)
# admin.site.register(ProductsInOrders)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'owner')
    list_display_links = ('id', 'created', 'status', 'owner')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner')
    list_display_links = ('id', 'title', 'owner')


@admin.register(ProductsInOrders)
class ProductsInOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantite', 'price', 'owner', 'order', 'prod')
    list_display_links = ('id', 'quantite', 'price', 'owner', 'order', 'prod')
