# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.db.models.aggregates import Count
from django.db.models import F
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import status
# from rest_framework.

from stock.models import Product, Supplier, ProductType, Purchase, Property, Sale
from stock.serializers import ProductSerializer, SupplierSerializer, ProductTypeSerializer, PurchaseSerializer, PropertySerializer, SaleSerializer


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib
import socket
from pathlib import Path
from string import Template

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
        purchase_id = self.kwargs.get('purchase_pk')
        purchase = Purchase.objects.get(id=purchase_id)

        serializer.save(user=self.request.user, purchase=purchase)


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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['name']
    ordering_fields = '__all__'


    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(supplier_id= kwargs['pk']).count() > 0:
            return Response({'error': "supplier can not be deleted since it is associated with product"}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)



class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.annotate(product_count=Count('products')).all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAuthenticated]

    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(product_type_id= kwargs['pk'].count() > 0):
            return Response({'error': "supplier can not be deleted since it is associated with product"})
        return super().destroy(request, *args, **kwargs)
    



    
    

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    


class SaleViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def perform_destroy(self, instance):
        product = instance.product

        product.quantity += instance.quantity
        product.save()

        if product.quantity < product.threshold:
            self.generate_alert_email(product)

        return super().perform_destroy(instance)

    def get_queryset(self):
        product_ids = Product.objects.filter(
            user=self.request.user).values_list('sale', flat=True)
        return Sale.objects.filter(id__in=product_ids)


class StockProductViewSet(ListModelMixin, GenericViewSet, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['productname']

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        if Sale.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': "product can not be deleted since it is associated with sale"}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)



class LowStockProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user, quantity__lte=F('threshold'))






def generate_alert_email(self, product):

    message = MIMEMultipart()
    message["from"] = "SAMUEL ENDALE"
    message["to"] = "sifenbeshada613@gmail.com"
    message["subject"] = "this is test"
    # message.attach(
    #     MIMEText("this is my first email sent by SAMI using a python interpreter", "plain"))

    # here we can use a plain text like the upper one or we can create an  html template
    template = Template(Path(
        r"C:\Users\SAMI\Videos\PYTHON\HELLOWORLD\.vscode\chapter_nine_python_standard_library\template.html").read_text(encoding="utf-8"))
    body_part = template.substitute({"name": "SAMI"})
    message.attach(MIMEText(body_part, "html"))

    message.attach(MIMEImage(open(Path(
        r"C:\Users\SAMI\Videos\PYTHON\HELLOWORLD\.vscode\chapter_nine_python_standard_library\sami.jpg.jpg"), "rb").read()))
    print("fine")

    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            print("hello")
            smtp.starttls()  # transport layer security with this all the commands we send with server will be encrypted
            print("transporting")
            smtp.login("samipythontest@gmail.com",
                       "kbqrjimrtbstdxky")
            print("logged in")
            smtp.send_message(message)
            print("sent...")
    except socket.gaierror as ex:
        print(ex)
    except smtplib.SMTPAuthenticationError as e:
        print(e)