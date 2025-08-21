from django.urls import path, include

from rest_framework_nested import routers
from .views import BusinessProfileViewSet, BusinessCategoryViewSet

from haztever.reviews.views import ReviewViewSet
from haztever.reviews.views import ReviewPhotoViewSet

router = routers.SimpleRouter()
router.register(r'profiles', BusinessProfileViewSet, basename='businessprofiles')
router.register(r'categories', BusinessCategoryViewSet, basename='businesscategories')

profiles_router = routers.NestedSimpleRouter(router, r'profiles', lookup='business_profile')
profiles_router.register(r'reviews', ReviewViewSet, basename='business-reviews')

reviews_router = routers.NestedSimpleRouter(profiles_router, r'reviews', lookup='review')
reviews_router.register(r'photos', ReviewPhotoViewSet, basename='review-photos')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(profiles_router.urls)),
    path('', include(reviews_router.urls)),
]
