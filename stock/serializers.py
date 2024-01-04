from rest_framework import serializers
from stock.models import User,  Product, Supplier, ProductType, Purchase, Property


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ['id', 'user', 'productname',
                  'property', 'quantity', 'price',
                  'threshold', 'product_type',
                  'purchase', 'supplier']


class SupplierSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info']


class ProductTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'product_count']

    product_count = serializers.IntegerField(read_only=True)


class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()
    productlist = ProductSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['id', 'quantity', 'total_price', 'date', 'productlist']




class ProperySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Property
        fields = ['id', 'brand', 'size']
        
        
        