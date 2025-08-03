from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import BusinessProfileViewSet, BusinessCategoryViewSet

router = DefaultRouter()
router.register(r'profiles', BusinessProfileViewSet, basename='businessprofiles')
router.register(r'categories', BusinessCategoryViewSet, basename='businesscategories')

urlpatterns = [
    path('', include(router.urls))
]
