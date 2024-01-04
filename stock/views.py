# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
# from rest_framework.

from stock.models import User, Product, Supplier, ProductType, Purchase, Property
from stock.serializers import UserSerializer, ProductSerializer, SupplierSerializer, ProductTypeSerializer, PurchaseSerializer, ProperySerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'  #['productname', 'property', 'purchase',]
    search_fields = '__all__'
    ordering_fields = '_all__'

    
    
    def get_serializer_context(self):
        return {'request' : self.request}
    
    


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(supplier_id= kwargs['pk'].count() > 0):
            return Response({'error': "supplier can not be deleted since it is associated with product"})
        return super().destroy(request, *args, **kwargs)



class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.annotate(product_count=Count('products')).all()
    serializer_class = ProductTypeSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(product_type_id= kwargs['pk'].count() > 0):
            return Response({'error': "supplier can not be deleted since it is associated with product"})
        return super().destroy(request, *args, **kwargs)
    
    
    

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.annotate(product_count=Count('product')).all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    
    
    def perform_create(self, serializer):
    # Call the serializer's save method to create the Purchase instance
        purchase_instance = serializer.save()

        # Manually create associated Product instances using the purchase_instance data
        product_data_list = serializer.validated_data.get('productlist', [])
        for product_data in product_data_list:
            Product.objects.create(purchase=purchase_instance, **product_data)

        return purchase_instance
    



class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = ProperySerializer
    



