from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import BusinessProfileViewSet, BusinessCategoryViewSet

router = DefaultRouter()
router.register(r'profiles', BusinessProfileViewSet, basename='businessprofile')
router.register(r'categories', BusinessCategoryViewSet, basename='businesscategory')

urlpatterns = [
    path('', include(router.urls))
]
