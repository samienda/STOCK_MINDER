from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from stock.admin import productAdmin
from tags.models import TaggedItem
from stock.models import Product

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(productAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
