from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)



class ProductType(models.Model):
    name = models.CharField(max_length=255)


class Purchase(models.Model):
    productlist = models.ForeignKey('product', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    date = models.DateField(auto_now_add=True)



class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)



class Property(models.Model): 
    SMALL = 'S'
    EXTRA_SMALL = 'XS'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    DOUBLE_EXTRA_LARGE = 'XXL'

    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (EXTRA_SMALL, 'Extra Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
        (DOUBLE_EXTRA_LARGE, 'Double Extra Large'),
    )  

    ADIDAS = 'A'
    NIKE = 'N'
    PUMA = 'P'
    REEBOK = 'R'
    JORDAN = 'J'
    # we have to add a search fiel for brand and size
    BRAND_CHOICES = (
        (ADIDAS, 'Adidas'),
        (NIKE, 'Nike'),
        (PUMA, 'Puma'),
        (REEBOK, 'Reebok'),
        (JORDAN, 'Jordan'),
    )

    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=255)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productname = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    threshold = models.IntegerField(validators=[MinValueValidator(0)])


class Sale(models.Model):
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1.00)])
    date = models.DateField(auto_now_add=True)
    product = models.ManyToManyField(Product, on_delete=models.CASCADE)


