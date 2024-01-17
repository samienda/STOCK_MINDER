from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db.models import Count
from django.utils.html import format_html, urlencode, format_html
from django import forms
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from . import models

# Register your models here.


class inventoryFilter(admin.SimpleListFilter):
    title = 'Inventory Status'
    parameter_name = 'inventory_status'

    def lookups(self, request, model_admin) -> list[tuple[str, str]]:
        return [
            ('low', 'Low'),
            ('good', 'Good Enough')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'low':
            return queryset.filter(quantity__lte=5)
        if self.value() == 'good':
            return queryset.filter(quantity__gt=5)

@admin.register(models.User)
class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    list_editable = ['email', 'password']
    list_per_page = 20 
    search_fields = ['username__istartswith']


@admin.register(models.Product)
class productAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'product_type', 'property','supplier', 'purchase']
    actions = ['clear_inventory']
    list_display = ['productname', 'user', 'supplier', 'property', 'quantity', 'price', 'inventory_status', 'product_type']
    list_editable = ['property', 'supplier', 'price']
    list_filter = ['property', 'supplier', 'product_type', inventoryFilter]
    list_per_page = 20
    search_fields = ['productname__istartswith']


    @admin.display(ordering='quantity')
    def inventory_status(self, product):
        if product.quantity <= product.threshold:
            return 'Low'
        else:
            return 'Good Enough'
        
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(quantity=0)
        self.message_user(
            request, 
            f'{updated_count} products were successfully updated',
            # messages.ERROR
            )



@admin.register(models.Property)
class propertyAdmin(admin.ModelAdmin):
    list_display = ['brand', 'size', 'product_count']
    search_fields = ['brand__istartswith', 'size__istartswith']
    
    @admin.display(ordering='products_count') 
    def product_count(self, property):
        url = (
            reverse('admin:stock_product_changelist')
              + '?'
              + urlencode({
                    'property__id': str(property.id)
              }))
        return format_html('<a href="{}">{}</a>', url, property.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
    
    list_editable = ['size']
    list_display_links = ['brand']
    list_per_page = 20




@admin.register(models.ProductType)
class productTypeAdmin(admin.ModelAdmin):
    exclude = ['featured_product']
    list_display = ['name', 'product_count',]
    search_fields = ['name__istartswith']

    @admin.display(ordering='products_count') 
    def product_count(self, productType):
        url = (
            reverse('admin:stock_product_changelist')
              + '?'
              + urlencode({
                    'product_type__id': str(productType.id)
              }))
        return format_html('<a href="{}">{}</a>', url, productType.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )
    list_per_page = 20
    




@admin.register(models.Supplier)
class supplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']
    list_editable = ['contact_info']
    list_per_page = 20
    search_fields = ['name__istartswith']

@admin.register(models.Purchase)
class purchaseAdmin(admin.ModelAdmin):
    exclude = ['productlist']
    list_display = ['quantity', 'total_price', 'date']
    list_editable = ['total_price']
    list_display_links = ['quantity']
    list_per_page = 20
    search_fields = ['date__istartswith']


class SaleForm(forms.ModelForm):
    class Meta:
        model = models.Sale
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        return obj.productname

@admin.register(models.Sale)
class saleAdmin(admin.ModelAdmin):
    form = SaleForm
    # autocomplete_fields = ['product']
    list_display = ['quantity', 'total_price', 'date', 'display_product']
    list_editable = ['total_price']  
    list_display_links = ['quantity']
    list_per_page = 20

    def display_product(self, obj):
        return ", ".join([product.productname for product in obj.product.all()])
    display_product.short_description = 'Product'

@receiver(m2m_changed, sender=models.Sale.product.through)
def update_product_quantity(sender, instance, action, **kwargs):
    if action == 'post_add':
        for product in instance.product.all():
            product.quantity -= instance.quantity
            product.save()

m2m_changed.connect(update_product_quantity, sender=models.Sale.product.through)