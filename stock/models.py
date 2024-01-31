from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.contrib.auth import get_user_model
>>>>>>> 300a086501a5a9cd479ecbf0d22516c07c57cd3c
from django.core.validators import MinValueValidator  # , MaxValueValidator
=======
from django.core.validators import MinValueValidator #, MaxValueValidator

>>>>>>> class_schema
# Create your models here.




class ProductType(models.Model):
    name = models.CharField(max_length=255)
<<<<<<< HEAD
<<<<<<< HEAD
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
=======
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
>>>>>>> class_schema
=======

>>>>>>> 300a086501a5a9cd479ecbf0d22516c07c57cd3c
    
    def __str__(self) -> str:
        return self.name


class Supplier(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name



class Purchase(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
=======
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
>>>>>>> 300a086501a5a9cd479ecbf0d22516c07c57cd3c
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)], default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                      MinValueValidator(1.00)], default=0)
    date = models.DateField(auto_now_add=True)
=======
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    date = models.DateField(auto_now_add=True)
    productlist = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='productlist', null=True, blank=True)
>>>>>>> class_schema
    
    
    def __str__(self) -> str:
        return f'{self.date}'
    




class Property(models.Model): 
    brand = models.CharField(max_length=25)
    size = models.CharField(max_length=10)
    
    def __str__(self):
        return " BRAND - " + self.brand + " SIZE - " + self.size


class Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    productname = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    purchase = models.ForeignKey(
        Purchase, on_delete=models.PROTECT, related_name='productslist')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    threshold = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return f"{self.id} => {self.productname} => {self.product_type} => {self.property}"


class Sale(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        product = self.product

        if product.quantity < self.quantity:
            return False

        product.quantity -= self.quantity
        product.save()

        super().save(*args, **kwargs)
