# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter,OrderingFilter
# from rest_framework.

from stock.models import Product, Supplier, ProductType, Purchase, Property, Sale
from stock.serializers import ProductSerializer, SupplierSerializer, ProductTypeSerializer, PurchaseSerializer, ProperySerializer, SaleSerializer

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '_all__'
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['purchase_id'] = self.kwargs.get('purchase_pk')
        return context

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user, purchase_id=self.kwargs['purchase_pk'])


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(supplier_id= kwargs['pk'].count() > 0):
            return Response({'error': "supplier can not be deleted since it is associated with product"})
        return super().destroy(request, *args, **kwargs)

    # def get_queryset(self):
    #     product_ids = Product.objects.filter(
    #         user=self.request.user).values_list('supplier', flat=True)
    #     return Supplier.objects.filter(id__in=product_ids)





class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.annotate(product_count=Count('products')).all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]

    
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_ids = Product.objects.filter(
            user=self.request.user).values_list('purchase', flat=True)
        return Purchase.objects.filter(id__in=product_ids)


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = ProperySerializer
    permission_classes = [IsAuthenticated]


class SaleViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        product = instance.product

        product.quantity += instance.quantity
        product.save()

        return super().perform_destroy(instance)

    def get_queryset(self):
        product_ids = Product.objects.filter(
            user=self.request.user).values_list('sale', flat=True)
        return Sale.objects.filter(id__in=product_ids)

    # def generate_alert(self, instance):
    #     product = instance.product
    #     if product.quantity < product.treshold:
    #         return Response({'error': "product is less than 10"})
    #     return super().generate_alert(instance)


class StockProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
