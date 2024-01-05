from rest_framework import serializers
from stock.models import User,  Product, Supplier, ProductType, Purchase, Property, Sale


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        purchase_id = self.context['purchase_id']
        return Product.objects.create(purchase_id=purchase_id, ** validated_data)


    class Meta:
        model = Product
        fields = ['id', 'user', 'productname',
                  'property', 'quantity', 'price',
                  'threshold', 'product_type',
                  'supplier']


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
    productslist = ProductSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    quantity = serializers.ReadOnlyField()

    def get_total_price(self, purchase: Purchase):
        return sum([product.quantity * product.price for product in purchase.productslist.all()])


    class Meta:
        model = Purchase
        fields = ['id', 'quantity', 'total_price', 'date', 'productslist']




class ProperySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Property
        fields = ['id', 'brand', 'size']


class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity', 'total_price']
