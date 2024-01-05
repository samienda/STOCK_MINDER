# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter,OrderingFilter
# from rest_framework.

from stock.models import User, Product, Supplier, ProductType, Purchase, Property, Sale
from stock.serializers import UserSerializer, ProductSerializer, SupplierSerializer, ProductTypeSerializer, PurchaseSerializer, ProperySerializer, SaleSerializer

# Create your views here.



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '_all__'


    
    def get_serializer_context(self):
        return {'purchase_id': self.kwargs['purchase_pk']}

    def get_queryset(self):
        return Product.objects.filter(purchase_id=self.kwargs['purchase_pk'])

    



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
    queryset = Purchase.objects.annotate(
        product_count=Count('productslist')).all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = ProperySerializer
    

class SaleViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_destroy(self, instance):
        product = instance.product

        product.quantity += instance.quantity
        product.save()

        return super().perform_destroy(instance)


class StockProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
