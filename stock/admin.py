from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'user', 'product_type', 'supplier', 'property', 'quantity', 'price']
admin.site.register(models.Property)

admin.site.register(models.User)

admin.site.register(models.ProductType)

admin.site.register(models.Supplier)

admin.site.register(models.Purchase)    