from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('suppliers', views.SupplierViewSet)
router.register('producttypes', views.ProductTypeViewSet)
router.register('purchases', views.PurchaseViewSet)
router.register('properties', views.PropertyViewSet)


urlpatterns = router.urls
    

