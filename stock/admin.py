from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Property)

admin.site.register(models.User)

admin.site.register(models.ProductType)

admin.site.register(models.Supplier)