from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    list_editable = ['email', 'password']
    list_per_page = 10 


@admin.register(models.Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['productname', 'user', 'supplier', 'property', 'quantity', 'price', 'inventory_status', 'product_type']
    list_editable = ['property', 'supplier', 'quantity', 'price', 'product_type']
    list_per_page = 10

    @admin.display(ordering='quantity')
    def inventory_status(self, product):
        if product.quantity <= product.threshold:
            return 'Low'
        else:
            return 'Good Enough'



@admin.register(models.Property)
class propertyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'size']
    list_editable = ['size']
    list_display_links = ['brand']
    list_per_page = 10

@admin.register(models.ProductType)
class productTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'featured_product']
    list_editable = ['featured_product']
    list_per_page = 10

@admin.register(models.Supplier)
class supplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']
    list_editable = ['contact_info']
    list_per_page = 10

@admin.register(models.Purchase)
class purchaseAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'total_price', 'date', 'productlist']
    list_editable = ['total_price', 'productlist']
    list_display_links = ['quantity']
    list_per_page = 10

@admin.register(models.Sale)
class saleAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'total_price', 'date', 'display_product']
    list_editable = ['total_price']  # remove 'quantity' from list_editable
    list_display_links = ['quantity']  # 'quantity' can stay here
    list_per_page = 10

    def display_product(self, obj):
        return ", ".join([product.name for product in obj.product.all()])
    display_product.short_description = 'Product'