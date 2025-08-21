from rest_framework import serializers

from django.db.models import Avg

from .models import BusinessProfile
from .models import BusinessCategory

from haztever.catalog.serializers import ProductSerializer

class BusinessProfileSerializer(serializers.ModelSerializer):
    
    products = ProductSerializer(many=True, read_only=True)
    
    average_score = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = BusinessProfile
        
        fields = [
            'id',
            'business_name',
            'logo',
            'banner',
            'category',
            'whatsapp',
            'social_networks',
            'products',
            'average_score',
            'review_count',
        ]
        
        read_only_fields = ['user']
        
    def get_average_score(self, obj):
        return obj.reviews.aggregate(Avg('score'))['score__avg'] or 0.0

    def get_review_count(self, obj):
        return obj.reviews.count()
        
class BusinessCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessCategory
        
        fields = [
            'id',
            'name',
        ]