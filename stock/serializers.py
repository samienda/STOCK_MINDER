from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from stock.models import Product, Supplier, ProductType, Purchase, Property, Sale


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email']



class PropertySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Property
        fields = ['id', 'brand', 'size']


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer(read_only=True)
    property_str = serializers.SerializerMethodField()
    supplier_str = serializers.SerializerMethodField()
    product_type_str = serializers.SerializerMethodField()
    # property = PropertySerializer()
    


    class Meta:
        model = Product
        fields = ['id', 'user', 'productname',
                  'property', 'quantity', 'price',
                  'threshold', 'product_type',
                  'supplier', 'property_str', 'supplier_str', 'product_type_str']
        
        
    def get_property_str(self, obj):
        return str(obj.property)
    
    def get_supplier_str(self, obj):
        return str(obj.supplier)
    
    def get_product_type_str(self, obj):
        return str(obj.product_type)


class SupplierSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'user']


class ProductTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    products_under = serializers.SerializerMethodField()
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'products_under']

    def get_products_under(self, product_type: ProductType):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            return product_type.products.filter(user=request.user).count()



class PurchaseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()
    productslist = ProductSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    def get_total_price(self, purchase: Purchase):
        return sum([product.quantity * product.price for product in purchase.productslist.all()])

    def get_quantity(self, purchase: Purchase):
        return sum([product.quantity for product in purchase.productslist.all()])


    class Meta:
        model = Purchase
        fields = ['id', 'quantity', 'total_price',
                  'date', 'productslist', 'user']





class SaleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    product_str = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity', 'total_price', 'user', 'date', 'product_str']
        
    def get_product_str(self, obj):
        return str(obj.product)
    

