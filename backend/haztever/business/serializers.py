from rest_framework import serializers

from .models import BusinessProfile
from .models import BusinessCategory

from haztever.catalog.serializers import ProductSerializer

class BusinessProfileSerializer(serializers.ModelSerializer):
    
    products = ProductSerializer(many=True, read_only=True)
    
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
            'products'
        ]
        
        read_only_fields = ['user']
        
class BusinessCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessCategory
        
        fields = [
            'id',
            'name',
        ]