from rest_framework import parsers
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .models import ReviewPhoto

from haztever.business.models import BusinessProfile

from .serializers import ReviewSerializer
from .serializers import ReviewPhotoSerializer

class ReviewViewSet(ModelViewSet):
    
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        business_pk = self.kwargs['business_profile_pk']
        return Review.objects.filter(business__pk=business_pk)
    
    def perform_create(self, serializer):
        business_pk = self.kwargs['business_profile_pk']
        business_profile = BusinessProfile.objects.get(pk=business_pk)
        serializer.save(business=business_profile)
        
class ReviewPhotoViewSet(ModelViewSet):
    
    serializer_class = ReviewPhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return ReviewPhoto.objects.filter(review_id=self.kwargs['review_pk'])
    
    def perform_create(self, serializer):
        review = Review.objects.get(pk=self.kwargs['review_pk'])
        serializer.save(review=review)