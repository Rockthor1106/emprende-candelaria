from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet

from .models import BusinessProfile
from .models import Product
from .models import ProductCategory

from .serializers import ProductSerializer
from .serializers import ProductCategorySerializer

class ProductViewSet(ModelViewSet):
    
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        
        try:
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            return Product.objects.filter(business=business_profile)

        except BusinessProfile.DoesNotExist:
            return Product.objects.none()
        
    def perform_create(self, serializer): 
        business_profile = BusinessProfile.objects.get(user=self.request.user)
        serializer.save(business=business_profile)
        
class ProductCategoryViewSet(ModelViewSet):
    
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        
        try: 
            business_profile = BusinessProfile.objects.get(user=self.request.user)
            return ProductCategory.objects.filter(business=business_profile)
        
        except BusinessProfile.DoesNotExist:
            return ProductCategory.objects.none()
        
    def perform_create(self, serializer):
        business_profile = BusinessProfile.objects.get(user=self.request.user)
        serializer.save(business=business_profile)

        
        


