from rest_framework import serializers
from stock.models import Product, Supplier, ProductType, Purchase, Property


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productname', 'property', 'quantity']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'product_count']

    product_count = serializers.IntegerField(read_only=True)


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'total_price', 'date', 'product_count']

    product_count = serializers.IntegerField(read_only=True)


class ProperySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'brand', 'size']
        
        
        