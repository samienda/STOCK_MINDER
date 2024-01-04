from django.urls import path
from . import views
from rest_framework_nested import routers

# URLConf

router = routers.DefaultRouter()
# router.register('products', views.ProductViewSet)
router.register('suppliers', views.SupplierViewSet)
router.register('producttypes', views.ProductTypeViewSet)
router.register('purchases', views.PurchaseViewSet)
router.register('properties', views.PropertyViewSet)
router.register('users', views.UserViewSet)

purchases_router = routers.NestedDefaultRouter(
    router, 'purchases', lookup='purchase'
)
purchases_router.register(
    'products', views.ProductViewSet, basename='purchase-products'
)


urlpatterns = router.urls + purchases_router.urls
    

