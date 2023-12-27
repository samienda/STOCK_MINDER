from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from stock.models import Product, Supplier, ProductType, Purchase, Property

from stock.serializers import ProductSerializer, SupplierSerializer, ProductTypeSerializer, PurchaseSerializer, ProperySerializer

# Create your views here.


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def supplier_list(request):
    queryset = Supplier.objects.all()
    serializer = SupplierSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def supplier_detail(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    serialzer = SupplierSerializer(supplier)
    return Response(serialzer.data)


@api_view()
def productType_list(request):
    queryset = ProductType.objects.all()
    serialzer = ProductTypeSerializer(queryset, many=True)
    return Response(serialzer.data)


@api_view()
def productType_detail(request, id):
    producttype = get_object_or_404(ProductType, pk=id)
    serialzer = ProductTypeSerializer(producttype)
    return Response(serialzer.data)


@api_view()
def purchase_list(request):
    queryset = Purchase.objects.all()
    serializer = PurchaseSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def purchase_detail(request, id):
    purchase = get_object_or_404(Purchase, pk=id)
    serializer = PurchaseSerializer(purchase)
    return Response(serializer.data)



@api_view()
def property_list(request):
    queryset = Property.objects.all()
    serializer = ProperySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def property_detail(request, id):
    properties = get_object_or_404(Property, pk=id)
    serializer = ProperySerializer(properties)
    return Response(serializer.data)