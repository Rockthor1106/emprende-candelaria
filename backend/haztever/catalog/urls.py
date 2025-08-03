from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet
from .views import ProductCategoryViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('categories', ProductCategoryViewSet, basename='productcategories')

urlpatterns = [
    path('', include(router.urls))
]