from rest_framework import viewsets, permissions

from .models import BusinessProfile, BusinessCategory
from .serializers import BusinessProfileSerializer, BusinessCategorySerializer

class BusinessProfileViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return BusinessProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class BusinessCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = BusinessCategory.objects.all()
    serializer_class = BusinessCategorySerializer
    permission_classes = [permissions.AllowAny]