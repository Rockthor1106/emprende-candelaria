from rest_framework import viewsets, permissions

from .models import BusinessProfile, BusinessCategory

from .permissions import IsOwnerOrReadOnly

from .serializers import BusinessProfileSerializer, BusinessCategorySerializer

class BusinessProfileViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BusinessProfile.objects.filter(user=self.request.user)
        
        return BusinessProfile.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class BusinessCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = BusinessCategory.objects.all()
    serializer_class = BusinessCategorySerializer
    permission_classes = [permissions.AllowAny]