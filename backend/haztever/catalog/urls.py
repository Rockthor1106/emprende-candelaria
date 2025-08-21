from django.urls import path, include

from rest_framework_nested import routers

from .views import ProductViewSet
from .views import ProductCategoryViewSet
from .views import ProductPhotoViewSet

router = routers.SimpleRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'product-categories', ProductCategoryViewSet, basename='productcategories')

products_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
products_router.register(r'photos', ProductPhotoViewSet, basename='productphotos')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls))
]