from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('suppliers/', views.supplier_list),
    path('suppliers/<int:id>/', views.supplier_detail),
    path('producttypes/', views.productType_list),
    path('producttypes/<int:id>/', views.productType_detail),
    path('purchases/', views.purchase_list),
    path('purchases/<int:id>/', views.purchase_detail),
    path('properties/', views.property_list),
    path('properties/<int:id>/', views.property_detail),
]
