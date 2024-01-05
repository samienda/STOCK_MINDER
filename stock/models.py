from django.db import models
from django.core.validators import MinValueValidator  # , MaxValueValidator
# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    
    def __str__(self) -> str:
        return self.username



class ProductType(models.Model):
    name = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    
    def __str__(self) -> str:
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name



class Purchase(models.Model):
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)], default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
                                      MinValueValidator(1.00)], default=0)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.date}'
    




class Property(models.Model): 
    brand = models.CharField(max_length=25)
    size = models.CharField(max_length=10)
    
    def __str__(self):
        return " BRAND - " + self.brand + " SIZE - " + self.size


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return f"{self.id} => {self.productname} {self.property}"


class Sale(models.Model):
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

    


